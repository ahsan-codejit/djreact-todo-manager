from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """Todo list serializer"""
    class Meta:
        model = Todo
        fields = (
            'id',
            'title',
            'description',
            'completed',
            'created_on',
            'updated_on'
        )