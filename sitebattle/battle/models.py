from django.db import models
from django.urls import reverse

class Menu(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name

class Members(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    content = models.TextField(blank=True, verbose_name='Информация')
    discord = models.URLField(max_length=200, unique=True, verbose_name='Дискорд')
    telegram = models.URLField(max_length=200, blank=True, verbose_name='Тг')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Слаг')
    points = models.IntegerField(verbose_name='Очки')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True, null=True, verbose_name='Фото')
    wins = models.IntegerField(verbose_name='Победы')
    loses = models.IntegerField(verbose_name='Поражения')
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('members')
    
    class Meta:
        verbose_name = 'Участники'
        verbose_name_plural = 'Участники'
        ordering = ['-points']

class Games(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название игры')
    url = models.URLField(max_length=100, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',null=True, blank=True, verbose_name='Фото')

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('games')
    
    class Meta:
        verbose_name = 'Игры'
        verbose_name_plural = 'Игры'