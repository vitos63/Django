from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import LoginUserForm, ProfileUser, RegisterCreateUser, UserPasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model


class LoginUser(LoginView):
    template_name = 'users/user_forms.html'
    form_class = LoginUserForm
    extra_context={'title': 'Авторизация', 'button':'Войти'}


class RegisterUser(CreateView):
    template_name = 'users/user_forms.html'
    form_class = RegisterCreateUser
    success_url = reverse_lazy('users:login')
    extra_context = {'title':'Регистрация пользователя', 'button':'Зарегистрироваться'}


class ProfileUser(LoginRequiredMixin, UpdateView):
    template_name = 'users/user_forms.html'
    form_class = ProfileUser
    extra_context = {'title':'Профиль пользователя', 'button':'Сохранить', 'links':{'Изменить пароль':'users:password_change'}}
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserChangePassword(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'users/user_forms.html'
    success_url = reverse_lazy('users:password_change_done')
    extra_context = {'title':'Смена пароля', 'button':'Сменить пароль'}
