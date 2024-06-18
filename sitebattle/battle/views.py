from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Menu, Members, Games

def index(request):
    menu = Menu.objects.all()
    data = {'menu': menu}
    return render(request, 'index.html', context=data)

def show_menu(request,menu_slug):
    menu = Menu.objects.all()
    post = get_object_or_404(Menu, slug = menu_slug)
    data = {'menu' : menu,
        'members': Members.objects.all(),
        'games': Games.objects.all(),
        }
    if post.slug == 'uchastniki':
        return render(request, 'members.html', context=data)
    elif post.slug == 'games':
        return render(request, 'games.html', context=data)


def member_info(request,member_slug):
    menu = Menu.objects.all()
    members = get_object_or_404(Members, slug = member_slug)
    data = {'menu': menu,
            'members': members,
            }
    return render(request, 'member_info.html', context=data)

def rule_games(request, rule_slug):
    menu = Menu.objects.all()
    games = get_object_or_404(Games, slug = rule_slug)
    data = {'menu': menu,
            'games': games,
            }
    return render(request, 'rule_games.html', context=data)