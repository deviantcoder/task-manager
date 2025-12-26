from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from apps.tasks.models import Project, Task

from .test_models import BaseTest


User = get_user_model()


class ProjectViewsTest(BaseTest):

    def setUp(self):
        super().setUp()

    def project_create(self):
        return Project.objects.create(
            author=self.user,
            title='Test Project'
        )

    def test_project_list_requires_login(self):
        response = self.client.get(
            reverse('tasks:project_list')
        )

        self.assertEqual(response.status_code, 302)

    def test_project_list_authenticated(self):
        self.client.login(
            username='testuser',
            password='testpass123'
        )

        response = self.client.get(
            reverse('tasks:project_list')
        )

        self.assertEqual(response.status_code, 200)


    def test_project_detail(self):
        self.client.login(
            username='testuser',
            password='testpass123'
        )

        project = self.project_create()
        
        response = self.client.get(
            reverse('tasks:project_detail', args=[project.id])
        )

        self.assertEqual(response.status_code, 200)

    def test_project_count(self):
        self.client.login(
            username='testuser',
            password='testpass123'
        )

        response = self.client.get(
            reverse('tasks:project_count')
        )

        project_count = self.user.projects.count()
        self.assertContains(response, f'{project_count} project')
