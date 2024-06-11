
from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'first_name', 'last_name', 'aadhaar_number')
    search_fields = ('first_name', 'last_name', 'aadhaar_number')
    list_filter = ('first_name', 'last_name')
    ordering = ('customer_id',)
    fields = ('first_name', 'last_name', 'aadhaar_number', 'customer_id')
    readonly_fields = ('customer_id',)

admin.site.register(Customer, CustomerAdmin)

