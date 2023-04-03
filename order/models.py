from django.db import models


class Order(models.Model):
    number = models.BigIntegerField(null=False)
    amount = models.IntegerField(null=False)
    weight = models.IntegerField(null=False)
    width = models.DecimalField(max_digits=5, decimal_places=1, null=False)
    height = models.DecimalField(max_digits=5, decimal_places=1, null=False)
    length = models.DecimalField(max_digits=5, decimal_places=1, null=False)
    zip_from = models.CharField(max_length=8, null=False)
    zip_to = models.CharField(max_length=8, null=False)
