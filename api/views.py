from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from portal.models import Robot
from api.serializers import RobotSerializer


@api_view(['GET', 'POST'])
def api_dashboard(request):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        tasks = Robot.objects.all()
        serializer = RobotSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RobotSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def api_detail(request, pk):
    """
    Get, udpate, or delete a specific task
    """
    try:
        task = Robot.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RobotSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RobotSerializer(task, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Create your views here.

# Create your views here.