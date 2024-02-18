# crm/admin.py

from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'acquisition_method','description', 'entry_time', 'owner', 'is_closed')
    list_filter = ('is_closed', 'entry_time', 'owner')
    search_fields = ('name', 'contact', 'acquisition_method')

