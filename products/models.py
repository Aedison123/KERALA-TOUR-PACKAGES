from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    image = models.ImageField(upload_to='product_images/')
    image2 = models.ImageField(upload_to='product_images/')
    days = models.CharField(max_length=100)

    def __str__(self):
        return self.name




