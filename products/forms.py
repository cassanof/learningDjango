# i actually made this file, django didnt give it to me!
from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "new-class-name two",
        "placeholder": "Your description",
        "id": "id-for-this-textarea",
        "rows": 10,
        "cols": 35,
    }))
    price = forms.DecimalField(initial=199.99)
