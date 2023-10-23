from django import forms
from category.models import Category


class ProductForm(forms.Form):
    title = forms.CharField(label='Product title')
    description = forms.CharField()
    price = forms.DecimalField()
    stock = forms.IntegerField()
    image = forms.ImageField ()
    category = forms.ModelChoiceField(Category.get_all(), required=False)

    
