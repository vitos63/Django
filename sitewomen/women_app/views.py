from typing import Any
from django.core.paginator import Paginator
from django.forms import BaseModelForm
from .utils import DataMixin
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.template.loader import render_to_string
from .models import Women, Category, TagPost
from .forms import AddPostForm, ContactForm
from django.views.generic import DetailView, ListView, CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'users:login'},
        ]


class Index(DataMixin, ListView):
    template_name = 'women_app/index.html'
    context_object_name = 'posts'
    cat_selected = 0
    def get_queryset(self):
        return Women.published.all()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)


def handle_uploaded_file(file):
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    with open(f'sitewomen/uploads/{now}_{file.name}', 'wb+') as des:
        for chunk in file.chunks():
            des.write(chunk)




@login_required()
def about(request):
    post = Women.published.all()
    paginator = Paginator(post, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    data = {
        'menu': menu,
        'title': 'О сайте',
        'page': page
            }
    return render(request, 'women_app/about.html', context = data)

class ShowPost(DataMixin,DetailView):
    template_name = 'women_app/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
    cat_selected = 1

    def get_object(self, queryset=None):
        return get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post'].title
        return context

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    success_url = reverse_lazy('home')
    template_name = 'women_app/addpage.html'
    title_page = 'Добавление статьи'

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'women_app/contact.html'
    success_url = reverse_lazy('home')
    title_page = 'Обратная связь'

    def get_form_kwargs(self):
        kwargs =  super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)



class ShowCategories(DataMixin, ListView):
    template_name = 'women_app/index.html'
    context_object_name = 'posts'

    def get_queryset(self) -> QuerySet[Any]:
        return Women.published.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.kwargs['cat_slug'])
        context['cat_selected'] = category.pk
        context['title'] = 'Рубрика' + category.name
        return context


class ShowTagPostlist(DataMixin,ListView):
    template_name = 'women_app/index.html'
    context_object_name = 'posts'

    def get_queryset(self) -> QuerySet[Any]:

        return Women.objects.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        tag = get_object_or_404(TagPost, slug=self.kwargs['tag_slug'])
        context['title'] = f'Тег: {tag.tag}'
        return context