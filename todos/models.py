from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class Todo(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('InProgress', 'InProgress'),
        ('Completed', 'Completed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    task_name = models.CharField(
        max_length=200,
        unique=True,
        validators=[MinLengthValidator(5)]
    )
    task_progress = models.CharField(
        max_length=300,
        choices=STATUS_CHOICES
    )
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.task_name} - {self.task_progress}'



