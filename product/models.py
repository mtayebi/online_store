from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext as _


# Create your models here.
class Product(BaseModel):
    pro_name = models.CharField(max_length=40, verbose_name=_('product_name'))
    brand = models.CharField(max_length=30, verbose_name=_('brand'))
    properties = models.TextField(max_length=1000, verbose_name=_('properties'))
    stock = models.PositiveIntegerField(default=0, verbose_name=_('stock'))
    discount = models.ForeignKey('Discount', on_delete=models.SET_DEFAULT, default=0, null=True, blank=True,
                                 verbose_name=_('discount'))
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name=_('category'))


