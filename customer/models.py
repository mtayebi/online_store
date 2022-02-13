from django.db import models
from core.models import BaseModel
from core.validators import validate_password, validate_phone
from django.utils.translation import gettext as _


# Create your models here.
class Address(BaseModel):
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    alley = models.CharField(max_length=50)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)


class Customer(BaseModel):
    first_name = models.CharField(max_length=30, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=30, verbose_name=_('last_name'))
    password = models.CharField(max_length=40, validators=[validate_password], verbose_name=_('password'))
    phone = models.CharField(max_length=11, validators=[validate_phone], verbose_name=_('phone'))
