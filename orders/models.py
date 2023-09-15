from django.db import models
from users.models import CustomUser
# Create your models here.
class OrderItem(models.Model):
    quantity = models.PositiveIntegerField()
    item_price = models.DecimalField()
