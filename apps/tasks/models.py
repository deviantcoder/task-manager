from uuid import uuid4

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    id = models.UUIDField(default=uuid4, unique=True, editable=False, primary_key=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ('author', '-created',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('tasks:project_detail', kwargs={'project_id': self.id})


class Task(models.Model):

    class PRIORITY_CHOICES(models.TextChoices):
        LOW = ('low', 'Low')
        MEDIUM = ('medium', 'Medium')
        HIGH = ('high', 'High')

    # Could be added later if functionality for shared projects is implemented
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

    title = models.CharField(max_length=200)

    priority = models.CharField(
        max_length=7, choices=PRIORITY_CHOICES.choices, default=PRIORITY_CHOICES.LOW
    )
    due_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    id = models.UUIDField(default=uuid4, unique=True, editable=False, primary_key=True)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ('project', '-created')

    def __str__(self):
        return self.title
