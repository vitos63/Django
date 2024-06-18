from django import template
import women_app.views as views
from ..models import Category

register = template.Library()

@register.inclusion_tag('women_app/list_categories.html')
def show_categories(cat_selected = 0):
    categories = Category.objects.all()
    return {'categories' : categories, 'cat_selected' : cat_selected}


