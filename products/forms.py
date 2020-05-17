# i actually made this file, django didnt give it to me!
from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "new-class-name two",
        "placeholder": "Your description",
        "id": "id-for-this-textarea",
        "rows": 10,
        "cols": 35,
    }))
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "dick" in title:
            raise forms.ValidationError("This is not a valid title")
        return title


class ProductNiceForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        "autocomplete": "off",
        "placeholder": " ",
    }))
    description = forms.CharField(label='', required=False, widget=forms.Textarea(attrs={
        "autocomplete": "off",
        "placeholder": " ",
        # "rows": 10,
        # "cols": 35,
    }))
    price = forms.DecimalField(label='', initial=199.99, widget=forms.TextInput(attrs={
        "autocomplete": "off",
        "placeholder": " ",
    }))

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "dick" in title:
            raise forms.ValidationError("This title contains profanity")
        return title

    def clean_description(self, *args, **kwargs):
        description = self.cleaned_data.get("description")
        if "dick" in description:
            raise forms.ValidationError("This description contains profanity")
        return description


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
