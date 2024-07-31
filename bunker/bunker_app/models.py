from django.db import models

class MemberCharact(models.Model):
    sex = models.CharField(max_length=100, verbose_name='Пол', null=True, choices={'M':'Мужик', 'F':'Псевдомужик'})
    age = models.IntegerField(verbose_name='Возраст', null=True)
    profession = models.CharField(max_length=250, verbose_name='Профессия', null=True)
    health = models.CharField(max_length=250, verbose_name='Здоровье', null=True)
    hobbii = models.CharField(max_length=250, verbose_name='Хобби', null=True)
    phobia = models.CharField(max_length=250, verbose_name='Фобия', null=True)
    baggage = models.CharField(max_length=250, verbose_name='Багаж', null=True)
    fact_1 = models.CharField(max_length=250, verbose_name='Факт-1', null=True)
    fact_2 = models.CharField(max_length=250, verbose_name='Факт-2', null=True)

    def __str__(self):
        return ' '.join([self.sex, self.age, self.profession])
    
    class Meta:
        verbose_name = 'Информация об игроках'
        verbose_name_plural = 'Информация об игроках'
    
