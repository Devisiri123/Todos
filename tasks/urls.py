from django.urls import path
from .views import (
    TaskListCreateView,
    TaskRetrieveUpdateDestroyView,
    AllTasksListView,
    ShareTaskView,
    SharedWithMeListView,
)

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('all-tasks/', AllTasksListView.as_view(), name='all-tasks-list'),
    path('share-task/', ShareTaskView.as_view(), name='share-task'),
    path('shared-with-me/', SharedWithMeListView.as_view(), name='shared-with-me'),
]




