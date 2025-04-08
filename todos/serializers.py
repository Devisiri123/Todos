from rest_framework import serializers
from .models import Todo
from users.serializers import UserSerializer


class TodoSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)
    class Meta:
        model = Todo
        fields = ['id', 'task_name', 'task_progress', 'user', 'user_details']
        read_only_fields = ['user']
        
        def create(self, validated_data):
            validated_data['user'] = self.context['request'].user
            return super().create(validated_data)

    def validate_task_name(self, value):
        # Check for duplicate task name
        if Todo.objects.filter(task_name=value).exists():
            raise serializers.ValidationError("Task name already exists.")
        return value

    def validate(self, data):
        # Check if the total number of tasks exceeds the limit (10)
        if Todo.objects.count() >= 10:
            raise serializers.ValidationError("Cannot add more than 10 tasks.")
        return data
    
   