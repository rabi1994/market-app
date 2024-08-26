from rest_framework import serializers
from ..models import Order,DeliveryData
from datetime import datetime
from ...products.serializers import ProductSerializer
from ...users.serializers import CustomerUserSerializer
class OrderSerializer(serializers.ModelSerializer):
    #products = ProductSerializer(many=True)
    #user = CustomerUserSerializer()
    class Meta:
        model = Order
        fields = '__all__'
        
    

   
