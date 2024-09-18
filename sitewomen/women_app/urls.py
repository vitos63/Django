from django.urls import path, register_converter
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import WomenSitemap


sitemaps = {
    'women' : WomenSitemap
}

urlpatterns = [
    path('', views.Index.as_view(), name='home'), #http://127.0.0.1:8000
    path('post/<slug:post_slug>', views.ShowPost.as_view(), name='post'), #http://127.0.0.1:8000/post/int/ 
    path('about/', views.about, name='about'), #http://127.0.0.1:8000/about/
    path('addpage/', views.AddPage.as_view(), name='add_page'), #http://127.0.0.1:8000/addpage
    path('contact/', views.ContactFormView.as_view(), name='contact'), #http://127.0.0.1:8000/contact
    path('categories/<slug:cat_slug>/', views.ShowCategories.as_view(), name='categories'), #http://127.0.0.1:8000/categories/int/
    path('tags/<slug:tag_slug>', views.ShowTagPostlist.as_view(), name='tag'),   #http://127.0.0.1:8000/tags/tag_slug/
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap')

]
