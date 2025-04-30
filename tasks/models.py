from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class SharedTask(models.Model):
    PERMISSION_CHOICES = (
        ('read', 'Read'),
        ('edit', 'Edit'),
    )

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='shared_tasks')
    shared_with = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_tasks')
    permission = models.CharField(max_length=10, choices=PERMISSION_CHOICES)

    class Meta:
        unique_together = ('task', 'shared_with')

    def __str__(self):
        return f"{self.shared_with.username} - {self.task.title} ({self.permission})"



                   
            







