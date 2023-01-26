from django.contrib import admin
from .models import Product, Category, Discount
from django.utils.translation import gettext as _


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('generic info'), {"fields": ('pro_name', 'brand', 'stock', 'image',
                                        'properties')}),
        (_('others'), {'fields': ('price', 'discount', 'category')}),
    )
    list_display = ['pro_name', 'category', 'brand', 'stock']
    list_filter = ['category', 'brand']


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ('generic info', {"fields": ('cat_title', 'parent_cat')}),
        ('others', {'fields': ('about',)}),
    )
    list_display = ['cat_title', 'parent_cat']
    list_filter = ['cat_title', 'parent_cat']


class DiscountAdmin(admin.ModelAdmin):
    fieldsets = (
        ('generic info', {"fields": ('discount_title', 'discount_amount', 'type')}),
        ('others', {'fields': ('max_value',)}),
    )
    list_display = ['discount_title', 'discount_amount', 'type']
    list_filter = ['discount_title', 'type']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Discount, DiscountAdmin)
