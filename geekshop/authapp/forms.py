from dataclasses import fields
from authapp.models import ShopUser

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

class LoginForm(AuthenticationForm):
    pass


class RegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', )


class UserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'image', 'email', 'city')

    def clean_city(self):
        if self.cleaned_data["city"] != 'Москва':
            raise forms.ValidationError("Только Москва")
        return self.cleaned_data["city"]


    
