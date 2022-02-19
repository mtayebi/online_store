from django.contrib import admin
from .models import Address, Customer
from django.utils.translation import gettext as _


# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    fieldsets = (
        ('generic info', {"fields": ('province', 'city', ('alley'))}),
        ('belongs to', {'fields': ('customer',)}),
    )
    list_display = ['address_owner', 'province', 'city', 'alley']
    list_filter = ['province', 'city', 'alley']

    @admin.display(description=_('address_owner'))
    def address_owner(self, obj):
        return f'{obj.customer.first_name}-{obj.customer.last_name}'


class CustomerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('customer info', {'fields': ('first_name', 'last_name', 'phone')}),
        ('customer private info', {'fields': ('password',)}),
    )
    list_display = ['first_name', 'last_name', 'phone']
    search_fields = ['first_name', 'last_name', 'phone']


admin.site.register(Address, AddressAdmin)
admin.site.register(Customer, CustomerAdmin)
