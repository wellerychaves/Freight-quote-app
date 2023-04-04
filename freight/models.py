from django.db import models


class Freight(models.Model):
    carrier = models.CharField(max_length=64)
    delivery_time = models.DateField()
    delivery_cost = models.DecimalField(max_digits=5, decimal_places=2)
    external_freight_id = models.IntegerField()

    order = models.ForeignKey(
        "order.Order",
        on_delete=models.CASCADE,
        related_name="freight",
    )
