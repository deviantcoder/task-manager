from django.test import TestCase
from django.contrib.auth import get_user_model

from apps.tasks.models import Project, Task


User = get_user_model()


class BaseTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )


class ProjectModelTest(BaseTest):

    def setUp(self):
        super().setUp()

    def test_project_create(self):
        project = Project.objects.create(
            author=self.user,
            title='Test Project'
        )

        self.assertEqual(project.title, 'Test Project')
        self.assertEqual(project.author, self.user)


class TaskModelTest(BaseTest):
    
    def setUp(self):
        super().setUp()
        self.project = Project.objects.create(
            author=self.user,
            title='Test Project'
        )

    def test_task_create(self):
        task = Task.objects.create(
            project=self.project,
            title='Test Task'
        )

        self.assertEqual(task.project, self.project)
        self.assertEqual(task.title, 'Test Task')
