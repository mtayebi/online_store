from django.db import models
from core.models import BaseModel, User
from core.validators import validate_password, validate_phone
from django.utils.translation import gettext as _


# Create your models here.
class Address(BaseModel):
    province = models.CharField(max_length=20, verbose_name=_("province"))
    city = models.CharField(max_length=20, verbose_name=_("city"))
    alley = models.CharField(max_length=50, verbose_name=_("alley"))
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)

    class Meta:
        verbose_name, verbose_name_plural = _('address'), _('addresses')

    def __str__(self):
        return f'{self.province}-{self.city}-{self.alley}'


class Customer(BaseModel):
    first_name = models.CharField(max_length=30, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=30, verbose_name=_('last_name'))
    password = models.CharField(max_length=40, validators=[validate_password], verbose_name=_('password'))
    # phone = models.CharField(max_length=11, validators=[validate_phone], verbose_name=_('phone'))
    user = models.OneToOneField(User, models.CASCADE)


    class Meta:
        verbose_name_plural, verbose_name = _('customers'), _('customer')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
        # return f'{self.user.first_name} {self.user.last_name}'
