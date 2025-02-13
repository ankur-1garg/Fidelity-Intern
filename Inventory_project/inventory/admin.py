from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price',
                    'created_by', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'created_by')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
