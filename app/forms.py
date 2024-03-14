from django import forms
from .models import Conges

class Conges_form(forms.ModelForm):
    class Meta:
        model = Conges
        fields = ['date_debut', 'date_fin']