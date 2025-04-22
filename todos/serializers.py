from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'task_name', 'task_progress', 'user']
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def validate_task_name(self, value):
        # Check if task name already exists
        if Todo.objects.filter(task_name=value).exists():
            raise serializers.ValidationError("Task name already exists.")
        return value

    def validate(self, data):
        # Limit total tasks per user to 10
        user = self.context['request'].user
        if Todo.objects.filter(user=user).count() >= 10:
            raise serializers.ValidationError("Cannot add more than 10 tasks.")
        return data


