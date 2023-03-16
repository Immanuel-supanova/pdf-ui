from django import forms

from django.contrib.auth.models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'permissions': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
