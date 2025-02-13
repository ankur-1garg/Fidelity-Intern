from django.db import models
from django.contrib.auth.models import User


class Inventory(models.Model):
    # Name of the inventory item
    name = models.CharField(max_length=200)
    # Optional description of the item
    description = models.TextField(null=True, blank=True)
    # Quantity of items in stock, defaults to 0
    quantity = models.IntegerField(default=0)
    # Price of the item with 2 decimal places
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Automatically set when item is created
    created_at = models.DateTimeField(auto_now_add=True)
    # Automatically updated whenever item is modified
    updated_at = models.DateTimeField(auto_now=True)
    # Foreign key to User model, cascading delete if user is removed
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # String representation of the item
        return self.name

    class Meta:
        # Sets plural name in admin interface
        verbose_name_plural = "Inventories"
