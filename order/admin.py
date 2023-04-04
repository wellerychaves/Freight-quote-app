from django.contrib import admin
from .models import Order
from .utils import get_package_info, get_freight_info

# from django.contrib.contenttypes.models import ContentType


@admin.action(description="Calculate freight")
def freight_calculator(self, request, queryset):
    order_selected = queryset.values()
    package_id = 0

    for item in order_selected:
        print(f"before: {item}")

        package_info = get_package_info(item)
        package_id = package_info[1]
        print(f"after: {package_info}")

        quoted_freight = get_freight_info(package_info[0])
        print(f"Quoted {quoted_freight}")

        # pegar o valor de quoted_freight e armazenar na model de freight


"""
    adicionando mensagem ao usuario após cotação.
self.message_user(
        request,
        ngettext(
            "%d story was successfully marked as published.",
            "%d stories were successfully marked as published.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )
 """


# admin.site.register(Order)
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
