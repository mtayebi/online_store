from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext as _
from customer.models import Customer
from product.models import Product

# Create your models here.
statuses = {
    ('Paid', _('paid')),
    ('Unpaid', _('unpaid')),
    ('Canceled', _('canceled')),
}


class OrderItem(BaseModel):
    number = models.PositiveIntegerField(verbose_name=_('order number'))
    order_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('order_product'))
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE, verbose_name=_('order_basket'))

    class Meta:
        verbose_name, verbose_name_plural = _('order_item'), _('order_items')


class DiscountCode(BaseModel):
    code_title = models.CharField(max_length=20, null=True, blank=True, verbose_name=_("code_title"))
    code_amount = models.PositiveIntegerField(verbose_name=_('code_amount'))

    class Meta:
        verbose_name, verbose_name_plural = _('discount_code'), _('discount_codes')

    def profit_value(self, price: int):
        return int(min(self.code_amount, price))


class Basket(BaseModel):
    basket_customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name=_('order_customer'))
    basket_code = models.ForeignKey(DiscountCode, on_delete=models.CASCADE, verbose_name=_('basket_code'), default=None)
    status = models.CharField(max_length=8, choices=statuses, default='Unpaid', verbose_name=_('basket_status'))

    class Meta:
        verbose_name, verbose_name_plural = _('basket'), _('baskets')

    @property
    def basket_paid(self):
        self.status = 'Paid'
        return self

    @property
    def basket_cancel(self):
        if self.status != 'Paid':
            self.status = 'Canceled'
        elif self.status == 'Paid':
            return Exception(_('you can not cancel a paid order'))

    @property
    def total_no_discount(self):
        total_value = 0
        for item in OrderItem.objects.filter(basket=self):
            total_value += item.order_product.price
            return total_value

    @property
    def basket_total_value(self):
        temp = self.total_no_discount()
        if self.basket_code:
            for item in OrderItem.objects.get(basket=self):
                if item.order_product.discount:
                    temp = temp-item.order_product.profit()

            temp = self.basket_code.profit_value(temp)
            return temp
        else:
            for item in OrderItem.objects.get(basket=self):
                if item.order_product.discount:
                    temp = temp-item.order_product.profit()
            return temp


