from django.contrib import admin
from .models import OrderItem,DiscountCode, Basket
from django.utils.translation import gettext as _


# Register your models here.
class OrderItemAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('order item info'), {"fields": ('number', 'order_product', 'basket',)}),
    )
    list_display = ['number', 'order_product', 'basket', 'item_category']
    list_display_links = ['number', 'order_product', 'basket']

    @admin.display(description=_('item_category'))
    def item_category(self, obj):
        return obj.order_product.category


class DiscountCodeAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('discount code info'), {"fields": ('code_amount', 'code_title',)}),
    )
    list_display = ['code_title', 'related_user']

    @admin.display(description=_("related_user"))
    def related_user(self, obj):
        return Basket.objects.get(basket_code=obj).basket_customer


class BasketAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('basket info'), {"fields": ('basket_customer',  'basket_code', 'status',)}),
    )
    list_display = ['basket_customer',  'basket_code', 'status']


admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(DiscountCode, DiscountCodeAdmin)
admin.site.register(Basket, BasketAdmin)

