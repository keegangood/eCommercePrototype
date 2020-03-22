from django.db import models
from django.contrib.auth.models import User
from inventory.models import Product

class Order(models.Model):
    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(null=True, blank=True)
    ordered_at     = models.DateTimeField(null=True, blank=True)
    grand_total    = models.DecimalField(default=0.0, decimal_places=2, max_digits=12)

class OrderItem(models.Model):
    product     = models.OneToOneField(Product, on_delete=models.PROTECT)
    order       = models.ManyToManyField(Order)
    quantity    = models.IntegerField(default=0)
    total_price = models.DecimalField(default=0.0, decimal_places=2, max_digits=12)

class OrderStatus(models.Model):
    STATUS_CHOICES = [
        ('o','Open'),
        ('p','Processing'),
        ('s','Shipped'),
        ('c','Completed')
    ]

    order  = models.OneToOneField(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='o')

