from rest_framework import status,viewsets
from ..models import User,BusinessUser
from ..serializers import UserSerializer, BusinessUserSerializer
from rest_framework.response import Response
import logging
def delete_user(user):
        user.delete()
        logging.warning("user got deleted because failed to create customer")
class BusinessViewSet(viewsets.ModelViewSet):
    queryset = BusinessUser.objects.all()
    serializer_class = BusinessUserSerializer
    '''
    def get_queryset(self):
        queryset = super().get_queryset()
        email = self.request.query_params.get('email',None)
        phone = self.request.query_params.get('phone',None)

        if email:
            queryset = queryset.filter(email=email)
        elif phone:
            queryset = queryset.filter(phone=phone)
        return queryset
    '''
          
    def create(self, request, *args, **kwargs):
        
        userSerializer = UserSerializer(data=request.data.pop('user'))
       
        if userSerializer.is_valid():
            user = userSerializer.save()
        
        logging.info(f"customer data {userSerializer.data['user_id']}")
        request.data['user_id']=userSerializer.data['user_id']
        customer_data = request.data
        customer_data['user'] = user.user_id
        try:
            serializer = BusinessUserSerializer(data=customer_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                delete_user(user)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            delete_user(user)
            
            return Exception('failed to create Customer')
    
    def list(self, request, *args, **kwargs):
        """
        Handle GET requests to list all customers.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        