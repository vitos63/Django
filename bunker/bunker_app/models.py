from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class MemberCharact(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Имя игрока', null=True)
    sex = models.CharField(max_length=100, verbose_name='Пол', null=True, choices={'Men':'Мужик', 'Woomen':'Женщина', 'Men barren': 'Мужчина бесплодный', 'Woomen barren': 'Женщина бесплодная'})
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

    
    class Meta:
        verbose_name = 'Информация об игроках'
        verbose_name_plural = 'Информация об игроках'
    
class Profession(models.Model):
    profession_en = models.CharField(max_length = 100, null=True)
    profession_ru = models.CharField(max_length = 100, null=True)

    def __str__(self):
        return self.profession_ru
    
class Health(models.Model):
    health_en = models.CharField(max_length = 100, null=True)
    health_ru = models.CharField(max_length = 100, null=True)
    
    def __str__(self):
        return self.health_ru


class Hobbii(models.Model):
    hobbii_en = models.CharField(max_length = 100, null=True)
    hobbii_ru = models.CharField(max_length = 100, null=True)
    
    def __str__(self):
        return self.hobbii_ru

class Phobia(models.Model):
    phobia_en = models.CharField(max_length = 100, null=True)
    phobia_ru = models.CharField(max_length = 100, null=True)

    def __str__(self):
        return self.phobia_ru
    
class Baggage(models.Model):
    baggage_en = models.CharField(max_length = 100, null=True)
    baggage_ru = models.CharField(max_length = 100, null=True)

    def __str__(self):
        return self.baggage_ru

class Fact(models.Model):
    fact_en = models.CharField(max_length=250, null = True)
    fact_ru = models.CharField(max_length=250, null = True)
    
    def __str__(self):
        return self.fact_ru