from django.contrib import admin
from .models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = [
        'trip_id',
        'pickup_datetime',
        'dropoff_datetime',
        'passenger_count',
        'total_amount'
    ]
    list_filter = ['payment_type', 'pickup_datetime']
    search_fields = ['pickup_location', 'dropoff_location']
    ordering = ['-pickup_datetime']
