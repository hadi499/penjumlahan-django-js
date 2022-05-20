from django import forms

from .models import Gaji2


class GajiForm(forms.ModelForm):
    class Meta:
        model = Gaji2
        fields = ['nama', 'gaji']
