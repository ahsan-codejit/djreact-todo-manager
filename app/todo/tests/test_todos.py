from django.test import TestCase

from todo.serializers import TodoSerializer
from todo.models import Todo

from rest_framework import status
from rest_framework.test import APIClient


class TestTodos(TestCase):
    """Test Todo Serializers"""
    def setUp(self):
        self.client = APIClient()

    def test_todo_list(self):
        payload = {
            "title": "test serializer",
            "description": "test serializer"
        }
        todos = Todo.objects.all().order_by('title')
        serializer = TodoSerializer(payload, many=True)
        self.assertEqual(todos.count(), serializer.data.count())
