from django import forms

from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
attrs = {'class': 'form-control'}


class UserLoginForm(AuthenticationForm):
    """ Tabel for login  """
    username = forms.CharField(label='Your name', widget=forms.TextInput(attrs=attrs))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs=attrs))
    captcha = CaptchaField()


class UserRegisterForm(UserCreationForm):
    """ Tabel for register user """
    username = forms.CharField(label='Your name', help_text='Max 150 char', widget=forms.TextInput(attrs=attrs))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs=attrs))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs=attrs))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs=attrs))

    class Meta:
        """ Fields which I used """
        model = User
        fields = ('username', 'email', 'password1', 'password2')