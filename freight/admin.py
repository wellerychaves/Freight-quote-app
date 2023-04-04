from django.contrib import admin

from .models import Freight


@admin.register(Freight)
class FreightAdmin(admin.ModelAdmin):
    pass
