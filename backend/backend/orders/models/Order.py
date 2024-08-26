from django.db import models
import uuid
from .DeliveryData import DeliveryData
from ...products.models import Product
from ...constants import DELIVERY_METHOD,PAYMENT_METHOD
from datetime import datetime
from ...users.models import Customer
class Order(models.Model):
    order_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(Customer,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    delivery_method= models.CharField(max_length=2,choices=DELIVERY_METHOD,default="TA")
    payment_method= models.CharField(max_length= 2 , choices=PAYMENT_METHOD,default='CA'),
    is_paid = models.BooleanField(default=False)
    order_date = models.DateField(default=datetime.now().date())
    order_time = models.TimeField(default=datetime.now().time())
    recieved_date = models.DateField(null=True,blank=True)
    recieved_time = models.TimeField(null=True,blank=True)
    
    def __str__(self):
        return f'order: {self.order_id} '
