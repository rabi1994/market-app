from rest_framework import serializers
from ..models import Order,DeliveryData
from datetime import datetime

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
    

   
