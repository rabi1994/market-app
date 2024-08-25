from rest_framework import serializers
from ..models import Order,DeliveryData
from datetime import datetime

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
    def create(self, validated_data):
        if 'delivery_data'in  validated_data: 
            delivery_data_data = validated_data.pop('delivery_data')
            delivery_data_ready = DeliveryData.objects.create(**delivery_data_data)
        else:
            delivery_data_ready = DeliveryData.objects.create( )
        order = Order.objects.create(delivery_data=delivery_data_ready, **validated_data)
        return order

   
