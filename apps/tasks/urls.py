from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<uuid:project_id>/', views.project_detail, name='project_detail'),
    path('projects/<uuid:project_id>/update/', views.project_update, name='project_update'),
    path('projects/<uuid:project_id>/delete/', views.project_delete, name='project_delete'),
]
