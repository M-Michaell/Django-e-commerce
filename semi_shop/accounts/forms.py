


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    first_name=forms.CharField(label="First Name", required=True)
    last_name=forms.CharField(label="Last Name", required=True)
    email=forms.EmailField(label="Email", required=True)


    class Meta(UserCreationForm.Meta):
        model=User
        fields=["first_name", "last_name", "email","username","password1","password2"]

    def clean_username(self):
        old_username = self.instance.username
        new_username = self.cleaned_data['username']

        if new_username == old_username:
            return new_username

        if new_username != old_username and User.objects.filter(username=new_username).exists():
            raise ValidationError("A user with that username already exists.")

        return new_username

