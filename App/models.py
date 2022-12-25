from django.db import models

# Create your models here.
class Product (models.Model):
    title = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=False) # null=True, default=True
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    amount = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    status = models.IntegerField(default=0) # 0: not in cart, 1: in cart
    