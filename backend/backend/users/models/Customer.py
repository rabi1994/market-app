from django.db import models
from .User import User
import uuid

class Customer(models.Model):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
    #TODO add location table( 2 fields tag and the current location) and attach them to the customer 
    location = models.CharField(max_length=255)


    
