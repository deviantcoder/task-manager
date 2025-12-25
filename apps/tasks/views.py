from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.views.decorators.http import require_http_methods
from django.http.response import HttpResponse

from .models import Task
from .forms import ProjectForm, TaskForm


# Project views


def get_project_queryset(request):
    return (
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


@login_required
def project_list(request):
    projects = get_project_queryset(request)

    context = {
        'projects': projects,
    }
    
    if request.htmx:
        return render(
            request, 'tasks/projects/partials/list_partial.html', context
        )

    return render(request, 'tasks/projects/list.html', context)


@login_required
def project_count(request):
    project_count = request.user.projects.count()
    context = {
        'project_count': project_count,
    }
    return render(
        request,
        'tasks/projects/partials/project_count.html',
        context
    )


@login_required
def project_detail(request, project_id):
    project = get_object_or_404(
        get_project_queryset(request),
        id=project_id
    )

    if request.htmx:
        context = {
            'project': project
        }

        response = render(
            request, 'tasks/projects/partials/header.html', context
        )

        return response

    context = {
        'project': project,
    }

    return render(request, 'tasks/projects/detail.html', context)


@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()

            if request.htmx:
                projects = get_project_queryset(request)

                context = {
                    'projects': projects,
                }

                response = render(
                    render,
                    'tasks/projects/partials/list_partial.html',
                    context,
                )
                response['HX-Trigger'] = '{"close": true, "project-changed": true}'

                return response
        else:
            return render(
                request, 'tasks/projects/partials/create_form.html', {'form': form}
            )
    
    form = ProjectForm()

    context = {
        'form': form,
    }

    return render(request, 'tasks/projects/partials/create_form.html', context)


@login_required
def project_update(request, project_id):
    project = get_object_or_404(
        get_project_queryset(request),
        id=project_id
    )

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()

            if request.htmx:
                context = {
                    'project': project
                }

                response = render(
                    request, 'tasks/projects/partials/header.html', context
                )
                response['HX-Trigger'] = '{"close": true, "project-changed": true}'

                return response
        else:
            return redirect('tasks:project_detail', project_id)
    else:
        form = ProjectForm(instance=project)

    context = {
        'form': form,
        'project': project,
    }

    return render(request, 'tasks/projects/partials/update.html', context)


@login_required
def project_delete(request, project_id):
    project = get_object_or_404(
        get_project_queryset(request),
        id=project_id
    )

    if request.method == 'POST':
        project.delete()
        return redirect('tasks:project_list')

    context = {
        'project': project
    }

    return render(request, 'tasks/projects/partials/delete.html', context)


# Task views


@require_http_methods(['POST'])
@login_required
def task_create(request, project_id):
    project = get_object_or_404(
        get_project_queryset(request),
        id=project_id
    )
    
    form = TaskForm(request.POST)

    if form.is_valid():
        task = form.save(commit=False)
        task.project = project
        task.save()

        if request.htmx:
            response = HttpResponse()
            response['HX-Trigger'] = '{"task-changed": true}'

            return response
    
    return redirect('tasks:project_detail', project_id)


@login_required
def task_delete(request, project_id, task_id):
    project = get_object_or_404(
        get_project_queryset(request),
        id=project_id
    )
    task = get_object_or_404(
        Task, id=task_id, project_id=project_id
    )

    if request.method == 'POST':
        task.delete()

        if request.htmx:
            response = HttpResponse()
            response['HX-Trigger'] = '{"close": true, "task-changed": true}'

            return response

        return redirect('tasks:project_detail', project_id)

    context = {
        'task': task,
        'project': project,
    }

    return render(request, 'tasks/tasks/partials/delete.html', context)


@login_required
def task_update(request, project_id, task_id):
    project = get_object_or_404(
        get_project_queryset(request),
        id=project_id
    )
    task = get_object_or_404(
        Task, id=task_id, project_id=project_id
    )

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

            if request.htmx:
                response = HttpResponse()
                response['HX-Trigger'] = '{"close": true, "task-changed": true}'

                return response

            return redirect('tasks:project_detail', project_id)
    else:
        form = TaskForm(instance=task)

    context = {
        'form': form,
        'task': task,
    }

    return render(request, 'tasks/tasks/partials/update.html', context)


@require_http_methods(['POST'])
@login_required
def task_toggle_complete(request, project_id, task_id):
    project = get_object_or_404(
        get_project_queryset(request),
        id=project_id
    )
    task = get_object_or_404(
        Task, id=task_id, project_id=project_id
    )

    task.is_completed = not task.is_completed
    task.save(update_fields=['is_completed'])

    if request.htmx:
        response = HttpResponse()
        response['HX-Trigger'] = '{"task-changed": true}'

        return response

    return redirect('tasks:project_detail', project_id)


@login_required
def task_list_partial(request, project_id):
    project = get_object_or_404(
        get_project_queryset(request),
        id=project_id
    )

    active_tasks = project.tasks.filter(is_completed=False)
    completed_tasks = project.tasks.filter(is_completed=True)

    context = {
        'active_tasks': active_tasks,
        'completed_tasks': completed_tasks,
    }

    return render(request, 'tasks/tasks/partials/list_partial.html', context)
