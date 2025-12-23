from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('projects/', views.project_list, name='project_list'),
    path('projects/<uuid:project_id>/', views.project_detail, name='project_detail'),
]
