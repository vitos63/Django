from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username','password']


class RegisterCreateUser(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels ={
            'username': 'Логин',
            'email':'E-mail'
            }
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError('Пользователь с таким E-mail уже существует')
        return email


class ProfileUser(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.TextInput(attrs={'class':'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'first_name':'Имя',
            'last_name':'Фамилия',
            }
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-input'}),
            'last_name':forms.TextInput(attrs={'class':'form-input'}),
        }
    
class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    new_password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class':'form-input'}))
