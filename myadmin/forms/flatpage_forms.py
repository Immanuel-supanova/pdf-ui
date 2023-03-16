from django import forms

from django.contrib.flatpages.models import FlatPage


class FlatPageForm(forms.ModelForm):
    template_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = FlatPage
        fields = '__all__'
        widgets = {
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'template_name': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'sites': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
