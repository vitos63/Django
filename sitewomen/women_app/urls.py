from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.Index.as_view(), name='home'), #http://127.0.0.1:8000
    path('post/<slug:post_slug>', views.ShowPost.as_view(), name='post'), #http://127.0.0.1:8000/post/int/ 
    path('about/', views.about, name='about'), #http://127.0.0.1:8000/about/
    path('addpage/', views.AddPage.as_view(), name='add_page'), #http://127.0.0.1:8000/addpage
    path('contact/', views.contact, name='contact'), #http://127.0.0.1:8000/contact
    path('login/', views.login, name='login'), #http://127.0.0.1:8000/login
    path('categories/<slug:cat_slug>/', views.ShowCategories.as_view(), name='categories'), #http://127.0.0.1:8000/categories/int/
    path('tags/<slug:tag_slug>', views.ShowTagPostlist.as_view(), name='tag'),   #http://127.0.0.1:8000/tags/tag_slug/

]
