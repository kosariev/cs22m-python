from django import forms
from coursework.models import Cars


class CarsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = "__all__"
