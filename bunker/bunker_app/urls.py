from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('calculat/', views.calculation, name='calculat'),
    path('clear/', views.clean_database, name='clear'),
]
