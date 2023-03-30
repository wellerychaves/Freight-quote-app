from django.contrib import admin
from .models import Order


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
