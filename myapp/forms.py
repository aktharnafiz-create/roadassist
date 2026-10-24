from django import forms
from .models import BreakdownRequest

class BreakdownForm(forms.ModelForm):
    class Meta:
        model = BreakdownRequest
        fields = ['customer_name', 'phone', 'problem', 'latitude', 'longitude']
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }