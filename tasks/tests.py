from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskModelTests(TestCase):
    def test_str_returns_title(self):
        task = Task.objects.create(title='Write report')
        self.assertEqual(str(task), 'Write report')

    def test_defaults_to_not_done(self):
        task = Task.objects.create(title='Write report')
        self.assertFalse(task.done)


class TaskListViewTests(TestCase):
    def test_list_view_status_code(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)

    def test_create_task_via_post(self):
        self.client.post(reverse('task_list'), {'title': 'Buy milk'})
        self.assertTrue(Task.objects.filter(title='Buy milk').exists())

    def test_toggle_task(self):
        task = Task.objects.create(title='Buy milk')
        self.client.post(reverse('task_toggle', args=[task.pk]))
        task.refresh_from_db()
        self.assertTrue(task.done)
