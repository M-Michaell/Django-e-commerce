from django import forms


class CategoryForm(forms.Form):
    name=forms.CharField()
    description = forms.CharField()
    image = forms.ImageField ()
    