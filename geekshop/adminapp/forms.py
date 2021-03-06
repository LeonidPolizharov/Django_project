from email.policy import default
from authapp.models import ShopUser
from mainapp.models import Category, Product
from django.forms.widgets import HiddenInput
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username',)

class UserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'image', 'email', 'city')


class CategoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget = HiddenInput()


class DiscountForm(forms.Form):
    discount = forms.DecimalField(
        max_value=100, 
        min_value=0,
        decimal_places=2, 
        required=True
    )