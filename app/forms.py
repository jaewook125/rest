from django import forms
from .models import Restaurant

class RestForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('restimage','restname','restsite',)
