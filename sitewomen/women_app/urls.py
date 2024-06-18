from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'), #http://127.0.0.1:8000
    path('post/<slug:post_slug>', views.show_post, name='post'), #http://127.0.0.1:8000/post/int/ 
    path('about/', views.about, name='about'), #http://127.0.0.1:8000/about/
    path('addpage/', views.addpage, name='add_page'), #http://127.0.0.1:8000/addpage
    path('contact/', views.contact, name='contact'), #http://127.0.0.1:8000/contact
    path('login/', views.login, name='login'), #http://127.0.0.1:8000/login
    path('categories/<slug:cat_slug>/', views.show_categories, name='categories'), #http://127.0.0.1:8000/categories/int/

]
