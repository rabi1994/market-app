from django.db import models
import uuid
from ...constants import DELIVERY_METHODS,STATUS
class Business(models.Model):
    business_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    business_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255,blank=True,null=True)
    type = models.CharField(max_length=20)
    delivery_method = models.CharField(max_length=2,choices=DELIVERY_METHODS,default="OD")
    status = models.CharField(max_length=10,choices=STATUS,default="closed")
    #opening_hours= models.One