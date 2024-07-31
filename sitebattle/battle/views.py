from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Menu, Members, Games

def index(request):
    menu = Menu.objects.all()
    members = Members.objects.all()
    data = {
        'menu': menu,
        'members': members        
        }
    return render(request, 'index.html', context=data)

def games(request):
    menu = Menu.objects.all()
    games = list(Games.objects.all())
    new_games = []
    for i in range(0,len(games),4):
        new_games.append(games[i:i+4])

    data = {'menu' : menu,
        'members': Members.objects.all(),
        'games': new_games,
                }
    return render(request, 'games.html', context=data)


def member_info(request):
    menu = Menu.objects.all()
    members = Members.objects.all()
    data = {'menu': menu,
            'members': members,
            }
    return render(request, 'members.html', context=data)

def rule_games(request, rule_slug):
    menu = Menu.objects.all()
    games = get_object_or_404(Games, slug = rule_slug)
    data = {'menu': menu,
            'games': games,
            }
    return render(request, 'rule_games.html', context=data)

def kvest(request):
    pass