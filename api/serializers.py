from rest_framework import serializers
from .models import Product, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'product')

class ProductSerializer(serializers.ModelSerializer):

    product_image = serializers.ImageField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'product_image')

