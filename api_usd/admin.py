from django.contrib import admin
from .models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("value", "request_date")
    search_fields = ("value",)
    list_filter = ("request_date",)
