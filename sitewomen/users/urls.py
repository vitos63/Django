from django.urls import path, register_converter
from . import views
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView


app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('password-change/', views.UserChangePassword.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name= 'users/password_done.html'), name='password_change_done'),
]
