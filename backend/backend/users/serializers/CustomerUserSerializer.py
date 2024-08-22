from rest_framework import serializers
from ..models import Customer,User
from ..serializers import UserSerializer
import logging
logger = logging.getLogger('myapp')
class CustomerUserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Customer
        fields = ['user','location']
        
        
    