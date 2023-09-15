from django.db import models
from orders.models import OrderItem

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
