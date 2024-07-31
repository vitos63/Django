from django.urls import path, register_converter
from . import views
from django.contrib.auth.views import LogoutView


app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'), 
]
