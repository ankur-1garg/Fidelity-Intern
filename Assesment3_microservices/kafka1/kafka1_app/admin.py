from django.contrib import admin
from .models import Price


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('item', 'item_id', 'price')
    list_filter = ('item',)
    search_fields = ('item', 'item_id')
    ordering = ('item_id',)
