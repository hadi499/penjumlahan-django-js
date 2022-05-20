from django.contrib import admin
from . models import Gaji, Gaji2


@admin.register(Gaji)
class GajiAdmin(admin.ModelAdmin):
    list_display = ['nama', 'gaji']
