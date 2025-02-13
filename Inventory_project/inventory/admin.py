from django.contrib import admin

# Import the Inventory model from models.py file
from .models import admin
from .models import Inventory

# Register the Inventory model with custom admin configuration
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    # Configure which fields to display in the admin list view
    list_display = ('name', 'quantity', 'price',
                    'created_by', 'created_at', 'updated_at')
    
    # Add filter options in the right sidebar
    list_filter = ('created_at', 'updated_at', 'created_by')
    
    # Enable search functionality for name and description fields
    search_fields = ('name', 'description')
    
    # Set default ordering to show newest items first
    ordering = ('-created_at',)
