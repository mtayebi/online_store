from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext as _


# Create your models here.
class Product(BaseModel):
    pro_name = models.CharField(max_length=40, verbose_name=_('product_name'))
    brand = models.CharField(max_length=30, verbose_name=_('brand'))
    image = models.ImageField(verbose_name=_('product_image'))
    properties = models.TextField(max_length=1000, verbose_name=_('properties'))
    stock = models.PositiveIntegerField(default=0, verbose_name=_('stock'))
    discount = models.ForeignKey('Discount', on_delete=models.SET_DEFAULT, default=0, null=True, blank=True,
                                 verbose_name=_('discount'))
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name=_('category'))

    class Meta:
        verbose_name, verbose_name_plural = _('product'), _('products')
        ordering = ['create_time']

    def __str__(self):
        return f'{self.brand}: {self.pro_name}'


class Category(BaseModel):
    parent_cat = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True, blank=True, verbose_name=_('parent_category'))
    cat_title = models.CharField(max_length=30, verbose_name=_('category_title'))
    about = models.TextField(max_length=500, verbose_name=_('about_category'))

    class Meta:
        verbose_name, verbose_name_plural = _('category'), _('categories')

    def __str__(self):
        return f'{self.cat_title}'


class Discount(BaseModel):
    discount_title = models.CharField(max_length=20, verbose_name=_('discount_title'))
    discount_amount = models.PositiveIntegerField(verbose_name=_('discount_amount'))
    type = models.CharField(max_length=10, choices=[(_('price'), _('Price')), (_('percent'), _('Percent'))],
                            verbose_name=_('discount_type'))
    max_value = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('max_discount_value'))

    class Meta:
        verbose_name, verbose_name_plural = _('discount'), _('discounts')

    def __str__(self):
        return f'{self.discount_title}'