from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import permissions, authentication
from rest_framework.response import Response
from to.models import Todo
from .serializers import Todoserializer


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([authentication.BasicAuthentication])
def gettodos(request):
    todos = Todo.objects.all()
    serializers = Todoserializer(todos, many=True)
    return Response(serializers.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([authentication.BasicAuthentication])
def gettodo(request, pk):
    todos = Todo.objects.get(id=pk)
    serializers = Todoserializer(todos, many=False)
    return Response(serializers.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([authentication.BasicAuthentication])
def create_todo(request):
    serializers = Todoserializer(data=request.data)

    if serializers.is_valid():
        serializers.save()

    return Response(serializers.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([authentication.BasicAuthentication])
def update_todo(request, pk):
    todos = Todo.objects.get(id=pk)
    serializers = Todoserializer(instance=todos, data=request.data)

    if serializers.is_valid():
        serializers.save()

    return Response(serializers.data)


@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([authentication.BasicAuthentication])
def delete_todo(request, pk):
    todos = Todo.objects.get(id=pk)
    serializers = Todoserializer(instance=todos, data=request.data)
    todos.delete()
    return Response('todo is deleted')
