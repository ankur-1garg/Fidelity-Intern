from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',
                    'roll_number', 'email', 'date_of_birth')
    search_fields = ('first_name', 'last_name', 'roll_number', 'email')
    list_filter = ('date_of_birth',)
    ordering = ('roll_number',)
