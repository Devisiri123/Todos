from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="todos"
    )
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('InProgress', 'InProgress'),
        ('Completed', 'Completed'),
    ]
    
    task_name = models.CharField(
        max_length=200,
        unique=True,  
        validators=[MinLengthValidator(5)]  
    )
    task_progress = models.CharField(
        max_length=300,
        choices=STATUS_CHOICES  
    )
    
    def __str__(self): 
        return f'{self.task_name} - {self.task_progress}'


