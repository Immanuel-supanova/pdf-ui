from django import forms

from .models import PdfDocument


class DocumentForm(forms.ModelForm):
    class Meta:
        model = PdfDocument
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'File Name e.g untitled'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
