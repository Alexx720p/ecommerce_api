from rest_framework import serializers
from .models import CartModel
from products.serializer import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = CartModel
        fields = ['product', 'quantity', 'added_at']