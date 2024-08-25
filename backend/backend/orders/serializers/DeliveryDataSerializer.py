from rest_framework import serializers
from ..models import DeliveryData

class DeliveryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryData
        fields = '__all__'
