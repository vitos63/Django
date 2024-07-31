from typing import Any
from django.contrib import admin, messages
from django.db.models.query import QuerySet
from .models import Women, Category
from django.utils.safestring import mark_safe

class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус женщины'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем')
            ]
    
    def queryset(self, request, queryset) :
        if self.value() == 'married':
            return queryset.filter(husband__isnull = False)
        else:
            return queryset.filter(husband__isnull = True)

@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'time_create', 'is_published', 'cat', 'content_length', 'show_photo']
    list_editable = ['is_published']
    list_display_links = ['id', 'title']
    ordering = ['-time_create', 'title']
    list_per_page = 5
    actions = ['published', 'unpublished']
    search_fields = ['title', 'cat__name']
    list_filter = [MarriedFilter,'is_published', 'cat__name']
    #prepopulated_fields = {'slug': ['title']}
    fields = ['title', 'is_published', 'content', 'cat', 'tags', 'show_photo', 'photo']
    readonly_fields = ['show_photo']

    @admin.display(description='Фото')
    def show_photo(self, women):
        if women.photo:
            return mark_safe(f'<img src="{ women.photo.url }"  width=50>')
        return f'Фото для {women.title}'

    @admin.display(description= 'краткое описание')
    def content_length (self, women):
        count = len(women.content)
        return f'Описание {count} символов'
    
    @admin.action(description= 'Опубликовать выбранные статьи')
    def published (self,request, queryset):
        count = queryset.update(is_published = Women.Status.PUBLISHED)
        self.message_user(request, message= f'Опубликовано {count} статей', level=messages.INFO)


    @admin.action(description= 'Снять с публикации выбранные статьи')
    def unpublished (self,request, queryset):
        count = queryset.update(is_published = Women.Status.DRAFT)
        self.message_user(request, message= f'Снято с публикации {count} статей', level=messages.WARNING)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

        
