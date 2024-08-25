from rest_framework import viewsets
from rest_framework.response import Response
from ..models import User
from ..serializers import UserSerializer
from rest_framework.decorators import api_view,action
from django.db.models import Q
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', None)
        if query:
            try:
                user = User.objects.get(
                    Q(email__exact=query) | Q(phone__exact=query)
                )
                serializer = self.get_serializer(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response({"error": "No customer found with the provided email or phone number"}, status=404)
            except User.MultipleObjectsReturned:
                return Response({"error": "Multiple customers found, but only one expected"}, status=400)
        else:
            return Response({"error": "No query parameter provided"}, status=400)
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