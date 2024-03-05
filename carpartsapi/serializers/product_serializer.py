from rest_framework import serializers
from carpartsapi.models.product_model import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
