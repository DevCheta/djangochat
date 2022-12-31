from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='products/', default='products/default.jpg')

