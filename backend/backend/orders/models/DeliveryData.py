from django.db import models 
from datetime import datetime
class DeliveryData(models.Model):
    order_date = models.DateField(default=datetime.now)
    order_time = models.TimeField(default=datetime.now)
    recieved_date = models.DateField(null=True,blank=True)
    recieved_time = models.TimeField(null=True,blank=True)
    