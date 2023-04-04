from django.db.models.signals import post_save
from django.dispatch import receiver
from order.models import Order
from datetime import datetime
import re


@receiver(post_save, sender=Order)
def generate_number(sender, instance, **kwargs):
    now = str(datetime.now())
    now = now[7:-3]
    now = int(re.sub(r"[-:. ]", "", now))

    if instance.number != now:
        instance.number = now
        instance.save()
