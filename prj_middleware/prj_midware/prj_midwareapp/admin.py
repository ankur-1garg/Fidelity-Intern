from django.contrib import admin
from .models import employee

@admin.register(employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_id', 'salary', 'doj')
    list_filter = ('doj',)
    search_fields = ('name', 'employee_id')
    ordering = ('employee_id',)
