from rest_framework import serializers
from order.serializers import OrderSerializer

from .models import Freight
from order.models import Order


class FreightSerializer(serializers.Serializer):
    carrier = serializers.CharField(max_length=64)
    delivery_time = serializers.DateField()
    delivery_cost = serializers.DecimalField(max_digits=5, decimal_places=2)
    external_freight_id = serializers.IntegerField()
    order = serializers.IntegerField()

    def create(self, validated_data: dict) -> Freight:
        order_id = validated_data.pop("order")
        order = Order.objects.get(pk=order_id)
        freight = Freight.objects.create(order=order, **validated_data)
        return freight
