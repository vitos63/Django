from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), #http://127.0.0.1:8000
    path('menu/<slug:menu_slug>', views.show_menu, name='menu'), #http://127.0.0.1:8000/menu/slug
    path('menu/uchastniki/<slug:member_slug>', views.member_info, name='members'), #http://127.0.0.1:8000/menu/uchastniki/slug
    path('menu/games/<slug:rule_slug>', views.rule_games, name='rule_games'), #http://127.0.0.1:8000/menu/games/slug

]
