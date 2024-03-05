from rest_framework import serializers
from carpartsapi.models.cart_model import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
