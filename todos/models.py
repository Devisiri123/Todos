from django.db import models

class Todo(models.Model):
    task_name=models.CharField(max_length=200)
    task_progress = models.CharField(max_length=300)
    
    def __str__(self): 
        return self.task_name + ' ' + self.task_progress