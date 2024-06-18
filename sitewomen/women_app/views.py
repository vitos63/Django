from django.shortcuts import render,redirect,get_object_or_404

from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.template.loader import render_to_string
from .models import Women, Category
# Create your views here.

menu = [{'title' : 'О сайте', 'url_name' : 'about'},
        {'title' : 'Добавить статью', 'url_name' : 'add_page'},
        {'title' : 'Обратная связь', 'url_name' : 'contact'},
        {'title' : 'Войти', 'url_name' : 'login'},
        ]




def index(request):
    post = Women.published.all()

    data = {'title': 'Главная страница',
            'menu': menu,
            'data_db': post,
            'cat_selected' : 0,
            }
    return render(request, 'women_app/index.html', context=data)


def about(request):
    data = {'title': 'О странице',
            'menu' : menu,
            }
    return render(request, 'women_app/about.html', context=data)


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug = post_slug)
    data = {'title': post.title,
            'menu': menu,
            'post' : post,
            'cat_selected' : 1,
            }
    return render(request, 'women_app/post.html', context=data)


def addpage(request):
    return HttpResponse('Добавление статьи')

def login(request):
    return HttpResponse('Авторизация')

def contact(request):
    return HttpResponse('Обратная связь')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Старница не найдена</h1>')

def show_categories(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id = category.pk)
    data = {'title': f'Рубрика {category.name}',
        'menu': menu,
        'data_db': posts,
        'cat_selected' : category.pk,
        }
    return render(request, 'women_app/index.html', context=data)
