from django.db import models
from django.urls import reverse

class Menu(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name

class Members(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    discord = models.URLField(max_length=200, unique=True)
    telegram = models.URLField(max_length=200, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('uchastniki')

class Games(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    rules = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('games')