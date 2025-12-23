from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q

from .models import Project


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
