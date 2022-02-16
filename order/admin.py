from django.contrib import admin
from .models import OrderItem,DiscountCode, Basket

# Register your models here.
class OrderItemAdmin(admin.ModelAdmin):
    pass


class DiscountCodeAdmin(admin.ModelAdmin):
    pass


class BasketAdmin(admin.ModelAdmin):
    pass


admin.site.regidter(OrderItem, OrderItemAdmin)
admin.site.register(DiscountCode, DiscountCodeAdmin)
admin.site.register(Basket, BasketAdmin)

