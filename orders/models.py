from django.db import models
from users.models import CustomUser
# Create your models here.
class OrderItem(models.Model):
    quantity = models.PositiveIntegerField()
    item_price = models.DecimalField()

class Order(models.Model):
    item_date = models.DateTimeField()
    total = models.DecimalField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)