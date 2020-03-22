from django.db import models

class Category(models.Model):
    name     = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Product(models.Model):

    UNITS = [
        ('floz', 'fluid ounce'),
        ('oz', 'ounce'),
        ('g', 'gram'),
        ('lb', 'pound'),
    ]

    title       = models.CharField(max_length = 100, blank = False)
    description = models.TextField(max_length = 1000, blank = False)
    price       = models.DecimalField(max_digits = 6, decimal_places = 2, default = 0.00)
    volume      = models.DecimalField(max_digits = 6, decimal_places = 2, default = 0.00)
    volume_unit = models.CharField(max_length = 100, choices = UNITS)

    quantity    = models.IntegerField(default = 0)
    category    = models.ManyToManyField(Category)

    def __str__(self):
        return self.title