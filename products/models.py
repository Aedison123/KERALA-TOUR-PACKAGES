# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    image = models.ImageField(upload_to='product_images/')
    image2 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    days = models.CharField(max_length=100)
    is_approved = models.BooleanField(default=False)  # New field to track approval status

    def __str__(self):
        return self.name
