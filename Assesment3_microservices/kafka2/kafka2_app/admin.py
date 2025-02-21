from django.contrib import admin
from .models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('district', 'state', 'pincode',
                    'population_density', 'last_updated')
    list_filter = ('state',)
    search_fields = ('district', 'state', 'pincode')
    readonly_fields = ('last_updated',)
    ordering = ('state', 'district')
    list_per_page = 20

    fieldsets = (
        ('Location Details', {
            'fields': ('pincode', 'district', 'state')
        }),
        ('Additional Information', {
            'fields': ('population_density', 'district_headquarters')
        }),
        ('System Fields', {
            'fields': ('last_updated',),
            'classes': ('collapse',)
        })
    )
