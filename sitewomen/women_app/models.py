from django.db import models
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_published = Women.Status.PUBLISHED)

class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = (0, 'Чернговик')
        PUBLISHED = (1, 'Опубликовано')
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')
    published = PublishedManager()
    objects = models.Manager()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-time_create']
    
    def get_absolute_url(self):
        return reverse ('post', kwargs={'post_slug' : self.slug})
    

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('categories', kwargs={'cat_slug' : self.slug})

class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.tag

