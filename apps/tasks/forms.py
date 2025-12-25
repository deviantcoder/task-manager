from django import forms

from .models import Project, Task


class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('title',)


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'priority', 'due_date')
