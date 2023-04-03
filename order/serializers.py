from rest_framework.validators import UniqueValidator
from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    number = serializers.IntegerField(
        validators=[UniqueValidator(Order.objects.all(), message="this field has to be unique")]
    )
    amount = serializers.IntegerField(min_value=0)
    weight = serializers.IntegerField(min_value=0)
    width = serializers.DecimalField(max_digits=5, decimal_places=1)
    height = serializers.DecimalField(max_digits=5, decimal_places=1)
    length = serializers.DecimalField(max_digits=5, decimal_places=1)
    zip_from = serializers.CharField(max_length=8)
    zip_to = serializers.CharField(max_length=8)
