from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_holder', 'account_number',
                    'balance', 'account_type', 'branch')
    search_fields = ('account_holder', 'account_number')
    list_filter = ('account_type', 'branch')
    readonly_fields = ('balance',)
