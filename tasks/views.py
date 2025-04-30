from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from django.db.models import Q
from .models import Task, SharedTask
from .serializers import TaskSerializer, SharedTaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        owned = Task.objects.filter(user=user)
        shared = Task.objects.filter(shared_tasks__shared_with=user)
        return (owned | shared).distinct()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(Q(user=user) | Q(shared_tasks__shared_with=user)).distinct()

    def perform_update(self, serializer):
        task = self.get_object()
        user = self.request.user

        if task.user == user:
            serializer.save()
        else:
            try:
                shared = SharedTask.objects.get(task=task, shared_with=user)
                if shared.permission == 'edit':
                    serializer.save()
                else:
                    raise PermissionDenied("You only have read permission.")
            except SharedTask.DoesNotExist:
                raise PermissionDenied("You do not have permission to edit this task.")

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied("Only the task owner can delete it.")
        instance.delete()

class AllTasksListView(generics.ListAPIView):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class ShareTaskView(generics.CreateAPIView):
    serializer_class = SharedTaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        task = serializer.validated_data['task']
        if task.user != self.request.user:
            raise PermissionDenied("Only the task owner can share it.")
        serializer.save()

class SharedWithMeListView(generics.ListAPIView):
    serializer_class = SharedTaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SharedTask.objects.filter(shared_with=self.request.user)









        
