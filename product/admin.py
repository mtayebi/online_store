from django.contrib import admin
from .models import Product, Category, Discount
from django.utils.translation import gettext as _


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('generic info'), {"fields": ('pro_name', 'brand', 'stock', 'image',
                                        'properties')}),
        (_('others'), {'fields': ('discount', 'category')}),
    )
    list_display = ['pro_name', 'category', 'brand', 'stock']
    list_filter = ['category', 'brand']


class CategoryAdmin(admin.ModelAdmin):
    pass


class DiscountAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Discount, DiscountAdmin)
