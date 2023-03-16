from django import forms
from django.contrib.redirects.models import Redirect


class RedirectForm(forms.ModelForm):
    class Meta:
        model = Redirect
        fields = '__all__'
        widgets = {
            'site': forms.Select(attrs={'class': 'form-control'}),
            'old_path': forms.TextInput(attrs={'class': 'form-control'}),
            'new_path': forms.TextInput(attrs={'class': 'form-control'}),
        }
