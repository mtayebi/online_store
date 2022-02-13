from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


# Create your models here.
class BaseManager(models.Manager):

    def get_queryset(self):
        return super.get_queryset().filter(is_deleted=False)

    def archiev(self):
        return super.get_queryset()


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
