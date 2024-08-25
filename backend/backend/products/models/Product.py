from django.db import models
import uuid
class Product(models.Model):
    product_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
def __str__(self):
    return self.name

