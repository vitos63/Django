from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.template.loader import render_to_string
# Create your views here.

menu=['О сайте','Добавить статью','Обратная связь','Войти']
data_db = [ {'id': 1, 'title': 'Анджелина Джоли', 'content': '''(англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.

    Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''', 'is_published': True},
            {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
            {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True}, 
            ]
menu = [{'title' : 'О сайте', 'url_name' : 'about'},
        {'title' : 'Добавить статью', 'url_name' : 'add_page'},
        {'title' : 'Обратная связь', 'url_name' : 'contact'},
        {'title' : 'Войти', 'url_name' : 'login'},
        ]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]


def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'data_db': filter(lambda x: x['is_published'] ,data_db),
            'cat_selected' : 0,
            }
    return render(request, 'women_app/index.html', context=data)


def about(request):
    data = {'title': 'О странице',
            'menu' : menu,
            }
    return render(request, 'women_app/about.html', context=data)


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id: {post_id} ')


def addpage(request):
    return HttpResponse('Добавление статьи')

def login(request):
    return HttpResponse('Авторизация')

def contact(request):
    return HttpResponse('Обратная связь')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Старница не найдена</h1>')

def show_categories(request, cat_id):
    data = {'title': 'Отображение по рубрикам',
        'menu': menu,
        'data_db': filter(lambda x: x['is_published'] ,data_db),
        'cat_selected' : cat_id,
        }
    return render(request, 'women_app/index.html', context=data)
