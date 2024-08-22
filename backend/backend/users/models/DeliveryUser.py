
from django.db import models
from .User import User
from backend.constants import DELIVERY_STATUS_CHOICES,DELIVERY_TYPE_CHOICES
class DeliveryUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length = 20, choices =DELIVERY_TYPE_CHOICES , default = 'standard')
    status = models.CharField(max_length= 20 , choices= DELIVERY_STATUS_CHOICES,default='offline')

    def __str__(self):
        return f"{self.user}"