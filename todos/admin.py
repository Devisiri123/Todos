from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_name', 'task_progress', 'user') 
    search_fields = ('task_name', 'user__username')             
    list_filter = ('task_progress',)                             

admin.site.register(Todo, TodoAdmin)






