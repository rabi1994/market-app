from django.db import models
from .User import User  # Assuming your User model is in user.py
from ...businesses.models import Business
class BusinessUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_id = models.ForeignKey(Business,max_length=255,on_delete=models.CASCADE)
    
    

    def __str__(self):
        return f"{self.business_name} ({self.user.email})"