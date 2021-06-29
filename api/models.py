from django.db import models

from BackEncryptTest.models import BaseModel
from django.utils.translation import gettext_lazy as _


class Course(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Курсы')
        verbose_name_plural = _('Курсы')
