from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q

from .models import Project
from .forms import ProjectForm


@login_required
def project_list(request):
    projects = (
        request.user.projects.all()
        .prefetch_related('tasks')
        .annotate(
            active_tasks_count=Count(
                'tasks', filter=Q(tasks__is_completed=False)
            ),
            completed_tasks_count=Count(
                'tasks', filter=Q(tasks__is_completed=True)
            )
        )
        .order_by('-created')
    )

    context = {
        'projects': projects,
    }

    return render(request, 'tasks/project_list.html', context)


@login_required
def project_detail(request, project_id):
    project = get_object_or_404(
        Project.objects.prefetch_related('tasks'),
        id=project_id
    )

    active_tasks = project.tasks.filter(is_completed=False)
    completed_tasks = project.tasks.filter(is_completed=True)

    context = {
        'project': project,
        'active_tasks': active_tasks,
        'completed_tasks': completed_tasks,
    }

    return render(request, 'tasks/project_detail.html', context)


@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save(update_fields=['author'])

            return redirect('tasks:project_list')
    else:
        form = ProjectForm()

    context = {
        'form': form,
    }

    return render(request, 'tasks/project_create.html', context)


@login_required
def project_update(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('tasks:project_detail', project_id)
    else:
        form = ProjectForm(instance=project)

    context = {
        'form': form,
    }

    return render(request, 'tasks/project_update.html', context)
