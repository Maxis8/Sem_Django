from django import forms

from HW_2 import models


class UpProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['title', 'description', 'price', 'count']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
        }

