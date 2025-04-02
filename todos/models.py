from django.db import models
from django.core.validators import MinLengthValidator

class Todo(models.Model):
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
        return self.task_name + ' ' + self.task_progress

