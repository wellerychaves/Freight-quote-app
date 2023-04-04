from django.contrib import admin

from .models import Freight


@admin.register(Freight)
class FreightAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "get_order_id",
        "carrier",
        "delivery_time",
        "delivery_cost",
        "external_freight_id",
    )

    # get only order id
    def get_order_id(self, object):
        return object.order.id

    get_order_id.short_description = "Order ID"
