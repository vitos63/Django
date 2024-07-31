from typing import Iterable
from django.db import models
from django.urls import reverse
from pytils.translit import slugify
from uuid import uuid4

class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_published = Women.Status.PUBLISHED)

class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = (0, 'Черновик')
        PUBLISHED = (1, 'Опубликовано')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True, null=True, default=None, verbose_name='Фото')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)), default=Status.DRAFT, verbose_name='Статус')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категории')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')
    husband = models.OneToOneField('Husband', on_delete=models.SET_NULL, related_name='wuman', null=True)
    published = PublishedManager()
    objects = models.Manager()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['-time_create']
    
    def get_absolute_url(self):
        return reverse ('post', kwargs={'post_slug' : self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args,**kwargs)
    

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('categories', kwargs={'cat_slug' : self.slug})
    
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.tag
    
    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug' : self.slug})

class Husband(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.name

