from django import forms
from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib.auth.models import User

from .models import NFT, Collection, Transaction, Tag, Review
from django import forms
from .models import NFT

class NFTForm(forms.ModelForm):
    class Meta:
        model = NFT
        fields = ['title', 'description', 'image', 'content_file']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['owner'].initial = user
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'shadow-sm appearance-none border rounded w-full py-3 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})
        self.fields['owner'].widget = forms.HiddenInput()

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['title', 'description']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['sender', 'receiver', 'nft', 'amount']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'nft', 'rating', 'comment']


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'shadow-sm appearance-none border rounded w-full py-3 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'shadow-sm appearance-none border rounded w-full py-3 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Enter password'}))

class RegisterForm(BaseUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'shadow-sm appearance-none border rounded w-full py-3 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Введите имя'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'shadow-sm appearance-none border rounded w-full py-3 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Введите фамилию'})
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'shadow-sm appearance-none border rounded w-full py-3 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Придумайте имя пользователя'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'shadow-sm appearance-none border rounded w-full py-3 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Введите эл. почту'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'shadow-sm appearance-none border rounded w-full py-3 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Придумайте пароль'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'shadow-sm appearance-none border rounded w-full py-3 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Подтвердите пароль'})

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )