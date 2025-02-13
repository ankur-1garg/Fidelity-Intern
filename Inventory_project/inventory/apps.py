from django.apps import AppConfig

# Configuration class for the inventory app
class InventoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"  # Default primary key field type
    name = "inventory"  # Name of the app