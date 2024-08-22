from django.db import models
from .User import User  # Assuming your User model is in user.py

class BusinessUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    
    

    def __str__(self):
        return f"{self.business_name} ({self.user.email})"