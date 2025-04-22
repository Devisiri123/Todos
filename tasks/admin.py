from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'created_at')  
    search_fields = ('title', 'description', 'user__username')
    list_filter = ('created_at',)  

