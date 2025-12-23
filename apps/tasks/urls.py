from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('projects/', views.project_list, name='project_list'),
]
