from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), #http://127.0.0.1:8000
    path('members/', views.member_info, name='members'), #http://127.0.0.1:8000/uchastniki
    path('games/', views.games, name='games'), #http://127.0.0.1:8000/games
    path('menu/games/<slug:rule_slug>', views.rule_games, name='rule_games'),
    path('kvest/', views.kvest, name='kvest'), #http://127.0.0.1:8000/menu/games/slug

]
