from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q


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
