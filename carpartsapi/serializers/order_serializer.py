from rest_framework import serializers
from carpartsapi.models.order_model import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
