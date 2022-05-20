from tabnanny import verbose
from django.db import models
from djmoney.models.fields import MoneyField


class Gaji(models.Model):
    nama = models.CharField(max_length=50)
    gaji = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Gaji'


class Gaji2(models.Model):
    nama = models.CharField(max_length=50)
    gaji = MoneyField(max_digits=14, decimal_places=2, default_currency='IDR')

    class Meta:
        verbose_name_plural = 'Gaji2'
