from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    """ Определяем поля для ЛОГИНа"""
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))


class UserRegisterForm(UserCreationForm):
    """Поля для регистрации"""

    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={"class": "form-control"}))
    help_text = 'Минимум 8 символов. Пароль не может состоять только из цифр.'
    password1 = forms.CharField(label='Пароль', help_text=help_text,
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        # определяем порядок полей
        fields = ('username', 'email', 'password1', 'password2')
        #
        # widgets = {
        #     'username': forms.TextInput(attrs={"class": "form-control"}),
        #     'email': forms.EmailInput(attrs={"class": "form-control"}),
        # }
