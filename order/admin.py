from django.contrib import admin, messages

from .models import Order
from .utils import get_package_info, get_freight_info
from freight.serializers import FreightSerializer


@admin.action(description="Calculate item freight")
def freight_calculator(self, request, queryset):
    order_selected = queryset.values()

    for item in order_selected:
        # send the selected package to filter the needed info and return a new dict.
        package_info = get_package_info(item)

        # stores the selected order id
        package_id = package_info[1]

        # stores filtered and quoted values
        quoted_freight = get_freight_info(package_info[0])

        # return example from quoted_freight:
        """ quoted_freight_example = {
            "carrier": "Jean shipments",
            "delivery_time": "2023-10-06",
            "delivery_cost": "100.0",
            "external_freight_id": 532,
        } """

        # add the package id before store in freight database
        quoted_freight.update(package_id)

        # Validates and save the package
        if len(quoted_freight) == 5:
            freight_serializer = FreightSerializer(data=quoted_freight)
            freight_serializer.is_valid(raise_exception=True)
            freight_serializer.save()
            self.message_user(request, "Cotação realizada e salva com sucesso!")
        else:
            self.message_user(request, "Houve um erro com o pedido relizado.", level=messages.ERROR)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "number",
        "amount",
        "weight",
        "width",
        "height",
        "length",
        "zip_from",
        "zip_to",
    )
    actions = [freight_calculator]
