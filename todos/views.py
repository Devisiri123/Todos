from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import HttpResponse

def welcome(request):
    response_data="Welcome to my Todo Project"
    return HttpResponse(response_data)

@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('task_progress', openapi.IN_QUERY, description="Filter by task progress (Pending, InProgress, Completed)", type=openapi.TYPE_STRING)
    ],
    responses={200: TodoSerializer(many=True)}
)
@swagger_auto_schema(
    method='post', 
    request_body=TodoSerializer,
    responses={201: TodoSerializer},
)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def todo_list(request):
    if request.method == 'GET':
        task_progress = request.GET.get('task_progress', None)  # Get from query param
        todos = Todo.objects.filter(user=request.user, is_deleted=False)
        if task_progress:
            todos = todos.filter(task_progress=task_progress)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='get',
    responses={200: TodoSerializer}
)
@swagger_auto_schema(
    method='put',
    request_body=TodoSerializer,
    responses={200: TodoSerializer}
)
@swagger_auto_schema(
    method='delete',
    responses={204: openapi.Response('Task soft-deleted')}
)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def todo_detail(request, id):
    try:
        todo = Todo.objects.get(pk=id, user=request.user)
    except Todo.DoesNotExist:
        return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        todo.is_deleted = True
        todo.save()
        return Response({"message": "Task deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

