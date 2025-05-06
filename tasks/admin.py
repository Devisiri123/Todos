from django.contrib import admin
from .models import Task, SharedTask

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'is_deleted', 'created_at')                 
    search_fields = ('title', 'description', 'user__username')
    list_filter = ('created_at', 'is_deleted')

@admin.register(SharedTask)
class SharedTaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'shared_with', 'permission')
    search_fields = ('task__title', 'shared_with__username')                                     




