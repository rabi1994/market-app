from rest_framework import viewsets,status,generics
from rest_framework.response import Response
from ..models import User
from ..serializers import UserSerializer
from rest_framework.decorators import api_view

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)
    
'''
import logging
@api_view(['GET'])
def getData(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)

    return Response(serializer.data)
@api_view(['POST'])
def setData(request):
    serializer = UserSerializer(data=request.data)
    logging.info(serializer)
    logging.info(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''