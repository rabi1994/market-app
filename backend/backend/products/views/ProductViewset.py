from rest_framework import viewsets
from rest_framework.response import Response
from ..models import Prodcut
from ..serializers import ProductSerializer
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Prodcut.objects.all()
    serializer_class =  ProductSerializer
    
