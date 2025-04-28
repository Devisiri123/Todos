from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'task_progress', 'user', 'is_deleted')
    search_fields = ('task_name',)
    list_filter = ('task_progress',)











