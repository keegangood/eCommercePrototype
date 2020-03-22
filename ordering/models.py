from django.db import models
from django.contrib.auth.models import User
from inventory.models import Product

class Order(models.Model):
    user           = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(null=True, blank=True)
    ordered_at     = models.DateTimeField(null=True, blank=True)
    grand_total    = models.DecimalField(default=0.0, decimal_places=2)
   
class OrderItem(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    product     = models.OneToOneField(Product)
    order       = models.ManyToManyField(Order)
    quantity    = models.IntegerField(default=0)
    total_price = models.DecimalField(default=0.0, decimal_places=2)

class OrderStatus(models.Model):
    STATUS_CHOICES = [
        ('o','Open'),
        ('p','Processing'),
        ('s','Shipped'),
        ('c','Completed')
    ]

    order  = models.OneToOneField(Order)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='o')

