from authapp.models import ShopUser
from mainapp.models import Category
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        exclude = ()

class UserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'image', 'email', 'city')


class CategoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'