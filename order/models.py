from django.db import models


class Order(models.Model):
    number = models.IntegerField()
    amount = models.IntegerField()
    weight = models.IntegerField()
    width = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    length = models.DecimalField(max_digits=5, decimal_places=2)
    zip_from = models.CharField(max_length=8)
    zip_to = models.CharField(max_length=8)
