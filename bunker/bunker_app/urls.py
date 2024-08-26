from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('members/<int:members_count>/<slug:disaster>', views.members_forms, name='members_forms'),
    path('calculat/<slug:disaster>', views.calculation, name='calculat'),
]
