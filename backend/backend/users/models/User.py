from django.db import models
from ...constants import ROLE_CHOICES
import uuid
from django.contrib.auth.hashers import make_password
class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(unique=True, max_length=254)
    phone = models.CharField(unique=True,max_length=15)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='regular')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    def set_password(self,raw_password):
        self.password = make_password(raw_password)
        
    