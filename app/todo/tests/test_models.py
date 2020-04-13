from django.test import TestCase

from todo import models


class TestModels(TestCase):
    """Test Todo Model"""

    def test_todo_str(self):
        data = {
            'title': 'Test Todo',
            'description': 'Test Todo description',
            'completed': False
        }
        todo = models.Todo.objects.create(**data)

        self.assertEqual(str(todo), data['title'])
