from django.contrib import admin
from .models import Members, Games
from django.utils.safestring import mark_safe

@admin.register(Members)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'content', 'points', 'show_photo']
    fields = ['name', 'content', 'points', 'photo']
    readonly_fields = ['show_photo']

    @admin.display(description='Фото')
    def show_photo(self,member):
        if member.photo:
            return mark_safe(f'<img src = "{member.photo.url}" width=50>')
        return f'Фото для {member.name}'

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display=['name', 'show_photo']
    fields = ['name', 'photo']
    readonly_fields = ['show_photo']

    @admin.display(description='Фото')
    def show_photo(self,game):
        if game.photo:
            return mark_safe(f'<img src = "{game.photo.url}" width=50>')
        return f'Фото для {game.name}'