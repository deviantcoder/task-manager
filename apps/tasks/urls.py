from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('projects/', views.project_list, name='project_list'),
    path('projects/count/', views.project_count, name='project_count'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<uuid:project_id>/', views.project_detail, name='project_detail'),
    path('projects/<uuid:project_id>/update/', views.project_update, name='project_update'),
    path('projects/<uuid:project_id>/delete/', views.project_delete, name='project_delete'),

    path('projects/<uuid:project_id>/tasks/', views.task_list_partial, name='task_list_partial'),
    path('projects/<uuid:project_id>/tasks/create/', views.task_create, name='task_create'),
    path('projects/<uuid:project_id>/tasks/<uuid:task_id>/update/', views.task_update, name='task_update'),
    path('projects/<uuid:project_id>/tasks/<uuid:task_id>/delete/', views.task_delete, name='task_delete'),
    path('projects/<uuid:project_id>/tasks/<uuid:task_id>/complete/', views.task_toggle_complete, name='task_toggle_complete'),
]
