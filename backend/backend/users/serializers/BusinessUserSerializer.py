from rest_framework import serializers
from ..models import BusinessUser

class BusinessUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUser
        fields = '__all__'
        
