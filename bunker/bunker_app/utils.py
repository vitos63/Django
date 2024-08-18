from random import randint
from .models import MemberCharact, Health
from django.db.models import Q, Min

infected = ['СПИД', 'Туберкулез', 'Коронавирус', 'Оспа']
with_stage = ['Шизофрения', 'Суицидальные наклонности', 'Была ампутация', 'Алкоголизм', 'Астма']
fatal = ['Рак', 'ИБС', 'Инсульт', 'Диабет', 'Почечная недостаточность', 'Агорофобия', 'Гелиофобия', 'Клаустрофобия']
baggage_5 = ['Набор снастей для рыбалки', 'Большой набор ниток', 'Патроны для охотничей винтовки', 'Инкубатор с куриными яйцами']
baggage_10 = ['Нож', 'Карта бункера и местности вокруг него', 'Газовая горелка', 'Радиоприемник', 'Книга по выживанию']
baggage_15 = ['Очиститель для воды', 'Сумка с медикаментами', 'Экзоскелет', 'Запас топлива']
profession_10 = ['Военный', 'Пчеловод', 'Географ', 'Кондитер', 'Кузнец', 'Уролог', 'Онколог', 'Гинеколог'] 
profession_15 = ['Охотник']
profession_20 = ['Механик', 'Киллер', 'Инженер', 'Гробовщик']
profession_30 = ['Доктор', 'Повар']
hobbii_5 = ['Дайвинг', 'Бег', 'Бокс', 'Альпинизм', 'Тяжелоатлет']
hobbii_10 = ['Радиотехника', 'Плотник', 'Стрельба', 'Психолог', 'Шитье']
hobbii_15 = ['Кулинария', 'Разведение животных', 'Охота', 'Ботаника', 'Рыбалка']
fact_minus_5 = ['Не говорит по-русски', 'Сидел в тюрьме за кражу', 'Аллергия на пыль', 'Эгоист', 'Рост 170, вес 50кг', 'Агрессивен',
'Эгоист', 'Рост 160, вес 100кг', 'Моется раз в месяц', 'Жадный']
fact_plus_5 = ['Хорошая физическая форма', 'Имеет лидерские качества', 'Работал в больнице', 'Чистоплотный', 'Служил в армии', 'Обучался стрельбе',
'Изучал очистку воды', 'Строил этот бункер', 'Проходил курсы урологии', 'Проходил курсы гинекологии']
fact_plus_10 = ['Работал инструктором по выживанию', 'Работал диетологом', 'Умеет добывать огонь', 'Умеет синтезировать топливо', 'Идеальные навыки оказания первой помощи', 'Выжил 30 дней на острове']


def remark(members):
    perfect_health = Health.objects.get(health_ru='Идеальное здоровье')
    if members.filter(profession__profession_ru='Уролог').exists():
        members.filter(sex='Men barren').update(sex='Men')
        print('Все бесплодные мужики стали нормальными, потому что есть Уролог')
    
    if members.filter(profession__profession_ru='Онколог').exists():
        members.filter(health__health_ru='Рак').update(health=perfect_health)
        print('Все больные раком излечились, потому что есть Онколог')
    
    if members.filter(profession__profession_ru='Гинеколог').exists():
        members.filter(sex='Woomen barren').update(sex='Woomen')
        print('Все бесплодные женщины стали нормальными, потому что есть Гинеколог')
    
    if members.filter(hobbii__hobbii_ru='Психолог').exists():
        members.filter(health__health_ru='Суицидальные наклонности').update(health=perfect_health)
        members.update(phobia=None)
        print('Суицидники излечились и пропали фобии, потому что есть Психолог')
    
    if members.filter(Q(fact_1__fact_ru='Проходил курсы урологии') | Q(fact_2__fact_ru='Проходил курсы урологии')).exists():
        min_age = members.filter(sex='Men barren').aggregate(Min('age'))['age__min']
        members.filter(sex='Men barren', age=min_age).update(sex='Men')
        print('Самый молодой бесплодный мужик стал нормальным, потому что есть человек, проходивший курсы урологии')

    if members.filter(Q(fact_1__fact_ru='Проходил курсы гинекологии') | Q(fact_2__fact_ru='Проходил курсы гинекологии')).exists():
        min_age = members.filter(sex='Woomen barren').aggregate(Min('age'))['age__min']
        members.filter(sex='Woomen barren', age=min_age).update(sex='Woomen')
        print('Самая молодая бесплодная женщина стал нормальной, потому что есть человек, проходивший курсы гинекологии')
    
    if members.filter(profession__profession_ru='Пчеловод').exists():
        members.filter(phobia__phobia_ru='Апифобия').update(alive=False)
        print('Люди с Апифобией умерли, потому что есть Пчеловод')
    
    if members.filter(profession__profession_ru='Клоун').exists():
        members.filter(phobia__phobia_ru='Клоунофобия').update(alive=False)
        print('Люди с Клоунофобией умерли, потому что есть Клоун')
    
    if members.filter(Q(profession__profession_ru='Переводчик') | Q(fact_1__fact_ru='Знает 5 языков') | Q(fact_2__fact_ru='Знает 5 языков')).exists():
        members.filter(fact_1__fact_ru = 'Не говорит по-русски').update(fact_1=None)
        members.filter(fact_2__fact_ru = 'Не говорит по-русски').update(fact_2=None)
        print('Теперь человек не разговаривающий на русском не получит минус очки')

def contamination(members):
    for i in members.filter(alive=True):
        current = i.health.health_ru
        
        if current in fatal or (i.phobia and i.phobia.phobia_ru in fatal):
            members.filter(pk=i.pk).update(alive=False)
            print(f'{i.name} умер, из-за смертельной болезни или фобии')
        
        elif current=='Шизофрения':
                for j in members.filter(alive=True):
                    if j.pk!=i.pk:
                        j.alive = False if randint(1,100)<i.stage else True
                        if not j.alive:
                            print(f'{j.name} умер из-за Шизофрении')
                        j.save()

        elif current in with_stage and randint(1,100)<i.stage:
            members.filter(pk=i.pk).update(alive=False)
            print(f'{i.name} Умер из-за болезни со стадией')
            
        elif current in infected:
            alive = False if randint(1,100)<70 else True
            if not alive:
                print(f'{i.name} умер от заражаемой болезни')
            members.filter(pk=i.pk).update(alive=alive)
            for j in members.filter(alive=True):
                if j.health.health_ru != current and randint(0,1):
                    print(f'{j.name} заразился болезнью {current}')
                    j.infection = j.infection + f', {current}' if j.infection else f'{current}'
                    j.alive = False if randint(1,100)<70 else True
                    if not j.alive:
                        print(f'{j.name} умер от заражаемой болезни')
                    j.save()
            
def breeding_score(members):
    breeding_points=0
    breeding_points+=10*members.filter(baggage__baggage_ru='Все необходимое для родов').count()
    members=members.filter(alive=True)
    breeding_points+=15*members.filter(Q(age__range=(18,34),sex='Woomen')).count()
    breeding_points+=10*members.filter(Q(age__range=(18,35), sex='Men') | Q(age__range=(35,50), sex='Woomen')).count()
    breeding_points+=5*members.filter(Q(sex='Men',age__gt=35) | Q(age__gt=50, sex='Woomen')).count()
    breeding_points+=10*members.filter(Q(profession__profession_ru='Порноактрисса') | Q(profession__profession_ru='Уролог') | Q(profession__profession_ru='Гинеколог')).count()
    breeding_points+=5*members.filter(health__health_ru='Нимфомания').count()
    breeding_points+=5*members.filter(Q(fact_1__fact_ru='Проходил курсы урологии') | Q(fact_1__fact_ru='Проходил курсы гинекологии') | Q(fact_1__fact_ru='Проходил курсы по минету')).count()
    breeding_points+=5*members.filter(Q(fact_2__fact_ru='Проходил курсы урологии') | Q(fact_2__fact_ru='Проходил курсы гинекологии') | Q(fact_2__fact_ru='Проходил курсы по минету')).count()
    breeding_points+=10*members.filter(Q(fact_1__fact_ru='Работал няней') | Q(fact_2__fact_ru='Работал няней')).count()
    return breeding_points

def survival_score(members):
    survival_points = 0
    for i in members.values('baggage__baggage_ru'):
        if i['baggage__baggage_ru'] in baggage_5:
            survival_points +=5
        
        elif i['baggage__baggage_ru'] in baggage_10:
            survival_points +=10
        
        elif i['baggage__baggage_ru'] in baggage_15:
            survival_points +=15

    members = members.filter(alive=True)
    survival_points += 10*members.filter(Q(sex='Men', age__range=(18,35)) | Q(sex = 'Men', age__gte=50) | Q(sex = 'Woomen', age__range=(35,50)) | Q(sex = 'Woomen barren', age__range=(35,50)) | Q(sex='Men barren', age__range=(18,35)) | Q(sex = 'Men barren', age__gte=50)).count()
    survival_points += 20*members.filter(Q(sex='Men', age__range=(36,49)) | Q(sex='Men barren', age__range=(36,49))).count()
    survival_points += 5*members.filter(Q(sex='Woomen', age__range=(18,35)) | Q(sex='Woomen barren', age__gte=50)).count()
    for i in members.values('profession__profession_ru', 'hobbii__hobbii_ru', 'fact_1__fact_ru','fact_2__fact_ru'):
        if i['profession__profession_ru'] in profession_10:
            survival_points +=10
        
        elif i['profession__profession_ru'] in profession_15:
            survival_points +=15
        
        elif i['profession__profession_ru'] in profession_20:
            survival_points +=20
        
        elif i['profession__profession_ru'] in profession_30:
            survival_points +=30
        
        if i['hobbii__hobbii_ru'] in hobbii_5:
            survival_points +=5
        
        elif i['hobbii__hobbii_ru'] in hobbii_10:
            survival_points +=10
        
        elif i['hobbii__hobbii_ru'] in hobbii_15:
            survival_points +=15
        
        if i['fact_1__fact_ru'] in fact_minus_5 or i['fact_2__fact_ru'] in fact_minus_5:
            survival_points -=5
            if i['fact_1__fact_ru'] in fact_minus_5 and i['fact_2__fact_ru'] in fact_minus_5:
                survival_points-=5
        
        if i['fact_1__fact_ru'] in fact_plus_5 or i['fact_2__fact_ru'] in fact_plus_5:
            survival_points +=5
            if i['fact_1__fact_ru'] in fact_plus_5 and i['fact_2__fact_ru'] in fact_plus_5:
                survival_points+=5
            
        if i['fact_1__fact_ru'] in fact_plus_10 or i['fact_2__fact_ru'] in fact_plus_10:
            survival_points +=10
            if i['fact_1__fact_ru'] in fact_plus_10 and i['fact_2__fact_ru'] in fact_plus_10:
                survival_points+=10


    return survival_points

def total_score(members):
    remark(members)
    contamination(members)
    breeding_points = breeding_score(members)
    survival_points = survival_score(members)
    return breeding_points, survival_points



