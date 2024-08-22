from rest_framework import status,viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Customer
from ..serializers import CustomerUserSerializer,UserSerializer
import logging
'''
@api_view(['GET'])
def getData(request):
    users = Customer.objects.all()
    serializer = CustomerUserSerializer(users, many = True)

    return Response(serializer.data)

@api_view(['POST'])
def setData(request):
    serializer = CustomerUserSerializer(data=request.data)
    logging.warning(f' user: {user_serializer}')
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print(f"Serializer Errors: {serializer.errors}")  # Debug line
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
'''
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerUserSerializer
    
    def create(self, request, *args, **kwargs):
        
        userSerializer = UserSerializer(data=request.data.pop('user'))
        if userSerializer.is_valid():
            userSerializer.save()
        logging.info(f"from customerViewSet {userSerializer.data}")
        logging.info(f"customer data {userSerializer.data['user_id']}")
        request.data['user_id']=userSerializer.data['user_id']
        serializer = CustomerUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logging.info(f"customer data {serializer.data}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def list(self, request, *args, **kwargs):
        """
        Handle GET requests to list all customers.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        