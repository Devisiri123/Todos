# tasks/serializers.py

from rest_framework import serializers
from .models import Task, SharedTask

class TaskSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'is_completed',
            'created_at', 'updated_at', 'owner_username'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'owner_username']

class SharedTaskSerializer(serializers.ModelSerializer):
    shared_with_username = serializers.CharField(source='shared_with.username', read_only=True)
    task_title = serializers.CharField(source='task.title', read_only=True)
    owner_username = serializers.CharField(source='task.user.username', read_only=True)

    class Meta:
        model = SharedTask
        fields = [
            'id', 'task', 'task_title',
            'shared_with', 'shared_with_username',
            'permission', 'owner_username'
        ]











