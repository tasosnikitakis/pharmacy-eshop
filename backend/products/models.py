from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True) # Description can be optional
    category = models.CharField(max_length=100) # Category of the product
    brand = models.CharField(max_length=100) # Brand of the product
    stock = models.PositiveIntegerField(default=0) # Stock quantity, default to 0
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00) # Discount rate as a percentage
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) # Discounted price
    original_price = models.DecimalField(max_digits=10, decimal_places=2) # Original price of the product
    image = models.ImageField(upload_to='products/', blank=True) # Image field for product images

    def __str__(self):
        return self.name