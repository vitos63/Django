from django.urls import path, register_converter
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('password-change/', views.UserChangePassword.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name= 'users/password_done.html'), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(success_url = reverse_lazy('users:password_reset_done'), template_name = 'users/user_forms.html', email_template_name='users/password_reset_email.html', extra_context ={'title':'Сброс пароля', 'button':'Выслать'} ), name='password_reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(success_url=reverse_lazy('users:password_reset_complete'), template_name ='users/user_forms.html' ,extra_context={'title':'Задайте новый пароль','button':'Изменить пароль'}), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), name='password_reset_complete'),
]
