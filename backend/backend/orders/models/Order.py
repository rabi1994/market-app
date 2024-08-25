from django.db import models
import uuid
from .DeliveryData import DeliveryData
from ...products.models import Product
from ...constants import DELIVERY_METHOD,PAYMENT_METHOD
class Order(models.Model):
    order_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    delivery_method= models.CharField(max_length=2,choices=DELIVERY_METHOD,default="TA")
    payment_method= models.CharField(max_length= 2 , choices=PAYMENT_METHOD,default='CA'),
    is_paid = models.BooleanField(default=False)
    delivery_data = models.OneToOneField(DeliveryData,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f'order: {self.order_id} '
