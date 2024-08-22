from rest_framework import serializers
from ..models import BusinessUser

class BusinessUser(serializers.ModelSerializer):
    class Meta:
        model = BusinessUser
        fields = '__all__'
        
