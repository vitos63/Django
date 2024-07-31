from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView



class LoginUser(LoginView):
    template_name = 'users/login.html'
    form_class = LoginUserForm
    extra_context={'title': 'Авторизация'}

