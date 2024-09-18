from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from pytils.translit import slugify
import uuid


class Information(models.Model):
    name = models.CharField(max_length=150, null=True, verbose_name='Заголовок')
    info = models.TextField(null=True, verbose_name='Информация')


class Menu(models.Model):
    name = models.CharField(max_length=50, null=True)
    url_name = models.CharField(max_length=50, null=True)


class Rules(models.Model):
    name = models.CharField(max_length=150, null=True, verbose_name='Заголовок')
    info = models.TextField(null=True, verbose_name='Описание')
    

class Characteristics(models.Model):
    characteristic = models.CharField(max_length=150, verbose_name='Характеристика')
    description = models.TextField(verbose_name='Описание характеристики')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Пример характеристики', blank=True)


class MemberCharact(models.Model):
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    name = models.CharField(max_length = 100, verbose_name = 'Имя игрока', null=True)
    sex = models.CharField(max_length=100, verbose_name='Пол', null=True, choices={'Man':'Мужик', 'Woman':'Женщина', 'Man barren': 'Мужчина бесплодный', 'Woman barren': 'Женщина бесплодная'})
    age = models.PositiveIntegerField(verbose_name='Возраст', null=True)
    profession = models.ForeignKey('Profession', max_length=100, null=True,verbose_name='Профессия', on_delete = models.SET_NULL, related_name = 'profession')
    health = models.ForeignKey('Health', max_length=250,null=True, on_delete = models.SET_NULL, verbose_name='Здоровье', related_name = 'health')
    stage = models.PositiveIntegerField(verbose_name = 'Стадия', null=True, validators=[MaxValueValidator(100, message='Значение должно быть меньше или равно 100')])
    hobbii = models.ForeignKey('Hobbii',max_length=250, verbose_name='Хобби', null=True,  on_delete = models.SET_NULL, related_name = 'hobbii')
    phobia = models.ForeignKey('Phobia', max_length=250, verbose_name='Фобия', null=True, on_delete = models.SET_NULL, related_name = 'phobia')
    baggage = models.ForeignKey('Baggage', max_length=250, verbose_name='Багаж', null=True, on_delete = models.SET_NULL, related_name = 'baggage')
    fact_1 = models.ForeignKey('Fact', max_length=250, verbose_name='Факт-1', null=True, on_delete = models.SET_NULL, related_name = 'fact_1')
    fact_2 = models.ForeignKey('Fact',max_length=250, verbose_name='Факт-2', null=True, on_delete = models.SET_NULL, related_name = 'fact_2')
    infection = models.CharField(max_length=250, verbose_name = 'Заражения', null=True)
    alive = models.BooleanField(verbose_name = 'Живой', default = True)
    session_key = models.CharField(max_length=150, null=True)

    
    class Meta:
        verbose_name = 'Информация об игроках'
        verbose_name_plural = 'Информация об игроках'
    
class Profession(models.Model):
    profession_en = models.CharField(max_length = 100, null=True)
    profession_ru = models.CharField(max_length = 100, null=True)
    survival_points = models.IntegerField(default=0, verbose_name='Очки выживания')
    breeding_points = models.IntegerField(default=0, verbose_name='Очки размножения')

    def __str__(self):
        return self.profession_ru
    
class Health(models.Model):
    health_en = models.CharField(max_length = 100, null=True)
    health_ru = models.CharField(max_length = 100, null=True)
    infected = models.BooleanField(default=False, verbose_name='Заражаемая')
    with_stage = models.BooleanField(default=False, verbose_name='Со стадией')
    fatal = models.BooleanField(default=False, verbose_name='Смертельная')
    breeding_points = models.IntegerField(default=0, verbose_name='Очки размножения')
    
    def __str__(self):
        return self.health_ru


class Hobbii(models.Model):
    hobbii_en = models.CharField(max_length = 100, null=True)
    hobbii_ru = models.CharField(max_length = 100, null=True)
    survival_points = models.PositiveIntegerField(default=0, verbose_name='Очки выживания')
    
    def __str__(self):
        return self.hobbii_ru

class Phobia(models.Model):
    phobia_en = models.CharField(max_length = 100, null=True)
    phobia_ru = models.CharField(max_length = 100, null=True)
    fatal = models.BooleanField(default=False, verbose_name='Смертельная')

    def __str__(self):
        return self.phobia_ru
    
class Baggage(models.Model):
    baggage_en = models.CharField(max_length = 100, null=True)
    baggage_ru = models.CharField(max_length = 100, null=True)
    survival_points = models.PositiveIntegerField(default=0, verbose_name='Очки выживания')
    breeding_points = models.IntegerField(default=0, verbose_name='Очки размножения')

    def __str__(self):
        return self.baggage_ru

class Fact(models.Model):
    fact_en = models.CharField(max_length=250, null = True)
    fact_ru = models.CharField(max_length=250, null = True)
    survival_points = models.IntegerField(default=0, verbose_name='Очки выживания')
    breeding_points = models.IntegerField(default=0, verbose_name='Очки размножения')
    
    def __str__(self):
        return self.fact_ru

class Disasters(models.Model):
    disaster_en = models.CharField(max_length=250, null=True)
    disaster_ru = models.CharField(max_length=250, null=True)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.disaster_ru
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.disaster_en)
        return super().save(*args,**kwargs)


