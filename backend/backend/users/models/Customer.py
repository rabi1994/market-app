from django.db import models
from .User import User

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #TODO add location table( 2 fields tag and the current location) and attach them to the customer 
    location = models.CharField(max_length=255)


    
