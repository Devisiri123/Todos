from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'task_name', 'task_progress']

    def validate_task_name(self, value):
        
        if Todo.objects.filter(task_name=value).exists():
            raise serializers.ValidationError("Task name already exists.")
        return value

    def validate(self, data):
       
        if Todo.objects.count() >= 10:
            raise serializers.ValidationError("Cannot add more than 10 tasks.")
        return data

