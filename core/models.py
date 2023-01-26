from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, UserManager
from core.validators import validate_phone, validate_password
from django.utils.translation import gettext as _

# Create your models here.



class BaseManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def archiev(self):
        return super().get_queryset()


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=_("create_time"))
    update_time = models.DateTimeField(auto_now=True, verbose_name=_("update_time"))
    delete_time = models.DateTimeField(blank=True, null=True, verbose_name=_("delete_time"))
    is_deleted = models.BooleanField(default=False, verbose_name=_("deleted"))

    objects = BaseManager()

    class Meta:
        abstract = True
        ordering = ['-creat_time']

    def is_delete(self):
        self.is_deleted = True
        self.delete_time = timezone.now()
        self.save()


class MyUserManager(UserManager):
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    # first_name = models.CharField(max_length=30, verbose_name=_('first_name'))
    # last_name = models.CharField(max_length=30, verbose_name=_('last_name'))
    # password = models.CharField(max_length=40, validators=[validate_password], verbose_name=_('password'))
    phone = models.CharField(max_length=11, unique=True, validators=[validate_phone], verbose_name=_('phone'))

    USERNAME_FIELD = 'phone'

    objects = MyUserManager()
