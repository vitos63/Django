from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60 * 1440)(views.Index.as_view()), name='home'),
    path('count/',  cache_page(60 * 1440)(views.Count.as_view()), name='count'),
    path('members/',  views.members_forms, name='members_forms'),
    path('calculat/', views.calculation, name='calculat'),
    path('rules/',  cache_page(60 * 1440)(views.Rules.as_view()), name='rules'),
    path('characteristics/',  cache_page(60 * 1440)(views.DescriptionCharacteristics.as_view()), name='characteristics'),
    path('feedback/',  cache_page(60 * 1440)(views.Feedback.as_view()), name='feedback'),

]
