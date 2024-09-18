from random import randint
from .models import Health
from django.db.models import Q, Min, Sum
from django.db.models.query import QuerySet

class Calculation():
    def __init__(self, members:QuerySet, disaster:str):
        self.logs = []
        self.members = members
        self.disaster = disaster
        self.members_professions = members.values_list('profession__profession_ru', flat=True)
        self.members_facts = list(members.values_list('fact_1__fact_ru', flat=True)) + list(members.values_list('fact_2__fact_ru', flat=True))
        self.members_hobbii = members.values_list('hobbii__hobbii_ru', flat=True)
        self.perfect_health = Health.objects.get(health_ru='Идеальное здоровье')



    def remark(self):
        if 'Уролог' in self.members_professions:
            self.members.filter(sex='Man barren').update(sex='Man')
            self.logs.append('Все мужчины излечились от бесплодия, потому что есть Уролог')
    
        if 'Онколог' in self.members_professions:
            self.members.filter(health__health_ru='Рак').update(health=self.perfect_health)
            self.logs.append('Все больные раком излечились, потому что есть Онколог')
    
        if 'Гинеколог' in self.members_professions:
            self.members.filter(sex='Woman barren').update(sex='Woman')
            self.logs.append('Все бесплодные женщины стали нормальными, потому что есть Гинеколог')
    
        if 'Психолог' in self.members_hobbii:
            self.members.filter(health__health_ru='Суицидальные наклонности').update(health=self.perfect_health)
            self.members.update(phobia=None)
            self.logs.append('Суицидники излечились и пропали фобии, потому что есть Психолог')
    
        if 'Проходил курсы урологии' in self.members_facts:
            min_age = self.members.filter(sex='Man barren').aggregate(Min('age'))['age__min']
            young_man = self.members.filter(sex='Man barren', age=min_age)
            young_man.update(sex='Man')
            self.logs.append(f'Игрок {young_man.name} излечился от бесплодия, потому что есть человек, проходивший курсы урологии')

        if 'Проходил курсы гинекологии' in self.members_facts:
            min_age = self.members.filter(sex='Woman barren').aggregate(Min('age'))['age__min']
            young_woman = self.members.filter(sex='Woman barren', age=min_age)
            young_woman.update(sex='Woman')
            self.logs.append(f'Игрок {young_woman.name} излечился от бесплодия, потому что есть человек, проходивший курсы гинекологии')
        
        if 'Пчеловод' in self.members_professions:
            apiphobia = self.members.filter(phobia__phobia_ru='Апифобия')
            for i in apiphobia:
                self.logs.append(f'Игрок {i.name} умер от Апифобии, потому что есть Пчеловод')
            apiphobia.update(alive=False)
        
        if 'Клоун' in self.members_professions:
            clown =self.members.filter(phobia__phobia_ru='Клоунофобия')
            for i in clown:
                self.logs.append(f'Игрок {i.name} умер от Клоунофобии, потому что в бункере есть Клоун')        
            clown.update(alive=False)
        
        if 'Переводчик' in self.members_professions or 'Знает 5 языков' in self.members_facts:
            self.members.filter(fact_1__fact_ru = 'Не говорит по-русски').update(fact_1=None)
            self.members.filter(fact_2__fact_ru = 'Не говорит по-русски').update(fact_2=None)
        
        if self.disaster=='Ядерная зима':
            criophobia = self.members.filter(phobia__phobia_ru='Криофобия')
            for i in criophobia:
                self.logs.append(f'Игрок {i.name} умирает от Криофобии, потому что катастрофа {self.disaster}')
            criophobia.update(alive=False)
            self.members.filter(phobia__phobia_ru='Гелиофобия').update(phobia=None)
            self.logs.append(f'Гелиофобия больше не смертельна, потому что катастрофа {self.disaster}')
        
        if self.disaster=='Наводнение':
            aquaphobia = self.members.filter(phobia__phobia_ru='Аквафобия')
            for i in aquaphobia:
                self.logs.append(f'Игрок {i.name} умирает от Аквафобии, потому что катастрофа {self.disaster}')
            aquaphobia.update(alive=False)
        
        if self.disaster=='Пришествие дьявола':
            devilphobia = self.members.filter(phobia__phobia_ru='Демонофобия')
            for i in devilphobia:
                self.logs.append(f'Игрок {i.name} умирает от Демонофобии, потому что катастрофа {self.disaster}')
            devilphobia.update(alive=False)
        
        if self.disaster=='Засуха':
            termo_aridito_phobia =self.members.filter(Q(phobia__phobia_ru='Термофобия') | Q(phobia__phobia_ru='Аридитафобия'))
            for i in termo_aridito_phobia:
                self.logs.append(f'Игрок {i.name} умирает от {i.phobia.phobia_ru}, потому что катастрофа {self.disaster}')
            termo_aridito_phobia.update(alive=False)
        
        if self.disaster=='Инопланетяне':
            ufophobia = self.members.filter(phobia__phobia_ru='Уфофобия')
            for i in ufophobia:
                self.logs.append(f'Игрок {i.name} умирает от Уфофобии, потому что катастрофа {self.disaster}')
            ufophobia.update(alive=False)

    
    def contamination(self):
        for i in self.members.filter(alive=True):
            current = i.health
            
            if current.fatal or (i.phobia and i.phobia.fatal):
                self.members.filter(pk=i.pk).update(alive=False)
                if current.fatal:
                    self.logs.append(f'Игрок {i.name} умер, из-за болезни {current.health_ru}')
                else:
                    self.logs.append(f'Игрок {i.name} умер, из-за фобии {i.phobia.phobia_ru}')
            
            elif current.health_ru=='Шизофрения':
                    for j in self.members.filter(alive=True):
                        if j.pk!=i.pk:
                            j.alive = False if randint(1,100)<i.stage else True
                            if not j.alive:
                                self.logs.append(f'Игрок {j.name} умер из-за Шизофрении')
                            j.save()

            elif current.with_stage and randint(1,100)<i.stage:
                self.members.filter(pk=i.pk).update(alive=False)
                self.logs.append(f'Игрок {i.name} умер из-за болезни {current.health_ru}')
                
            elif current.infected:
                if current.health_ru!='СПИД открытый':
                    for j in self. members.filter(alive=True):
                        if j.health.health_ru != current.health_ru and randint(0,1):
                            self.logs.append(f'Игрок {j.name} заразился болезнью {current.health_ru}')
                            j.infection = j.infection + f', {current}' if j.infection else f'{current.health_ru}'
                            j.alive = False if randint(1,100)<70 else True
                            if not j.alive:
                                self.logs.append(f'Игрок {j.name} умер от болезни {current.health_ru}')
                            j.save()
                alive = False if randint(1,100)<70 else True
                if not alive:
                    self.logs.append(f'Игрок {i.name} умер от болезни {current.health_ru}')
                self.members.filter(pk=i.pk).update(alive=alive)
    
    def breeding_score(self):
        breeding_points=0
        breeding_points+=self.members.aggregate(Sum('baggage__breeding_points'))['baggage__breeding_points__sum']
        members_alive=self.members.filter(alive=True)
        breeding_points+=15*members_alive.filter(Q(age__range=(18,34),sex='Woman')).count()
        breeding_points+=10*members_alive.filter(Q(age__range=(18,35), sex='Man') | Q(age__range=(35,50), sex='Woman')).count()
        breeding_points+=5*members_alive.filter(Q(sex='Man',age__gt=35) | Q(age__gt=50, sex='Woman')).count()
        breeding_points+=self.members.aggregate(Sum('profession__breeding_points'))['profession__breeding_points__sum']
        breeding_points+=self.members.aggregate(Sum('health__breeding_points'))['health__breeding_points__sum']
        breeding_points+=self.members.aggregate(Sum('fact_1__breeding_points'))['fact_1__breeding_points__sum'] + self.members.aggregate(Sum('fact_2__breeding_points'))['fact_2__breeding_points__sum'] 
        
        return breeding_points
    

    def survival_score(self):
        survival_points = 0
        survival_points += self.members.aggregate(Sum('baggage__survival_points'))['baggage__survival_points__sum']
        members_alive = self.members.filter(alive=True)
        survival_points += 10*members_alive.filter(Q(sex='Man', age__range=(18,35)) | Q(sex = 'Man', age__gte=50) | Q(sex = 'Woman', age__range=(35,50)) | Q(sex = 'Woman barren', age__range=(35,50)) | Q(sex='Man barren', age__range=(18,35)) | Q(sex = 'Man barren', age__gte=50)).count()
        survival_points += 20*members_alive.filter(Q(sex='Man', age__range=(36,49)) | Q(sex='Man barren', age__range=(36,49))).count()
        survival_points += 5*members_alive.filter(Q(sex='Woman', age__range=(18,35)) | Q(sex='Woman barren', age__gte=50)).count()
        survival_points += self.members.aggregate(Sum('profession__survival_points'))['profession__survival_points__sum']
        survival_points += self.members.aggregate(Sum('hobbii__survival_points'))['hobbii__survival_points__sum']
        survival_points += self.members.aggregate(Sum('fact_1__survival_points'))['fact_1__survival_points__sum'] + self.members.aggregate(Sum('fact_2__survival_points'))['fact_2__survival_points__sum']

        return survival_points
    


def total_score(members,disaster):
    calculated_characteristics = Calculation(members, disaster)
    calculated_characteristics.remark()
    calculated_characteristics.contamination()
    breeding_points = calculated_characteristics.breeding_score() // members.all().count()
    survival_points = calculated_characteristics.survival_score() // members.all().count()
    logs = calculated_characteristics.logs

    return breeding_points, survival_points, logs


def reproduction(members, breeding_points, bunker_alive):
    chance_breed = 'Шанс размножения после выхода из бункера 0 %'
    bunker_breed = 'Бункер не размножился'
    members_count = members.filter(alive=True).count() 
    if bunker_alive=='Бункер выжил' and members_count>1 and members.filter(sex='Man').exists() and members.filter(sex='Woman').exists():
        if members_count%2==0:
            perfect_breed = 25*members_count//2
            chance_breed = (f'Шанс размножения после выхода из бункера {round(breeding_points/(perfect_breed/100),1)}%')
        else:
            perfect_breed = 10*members_count//2 + 15*(members_count//2 + 1)
            chance_breed = (f'Шанс размножения после выхода из бункера {round(breeding_points/(perfect_breed/100),1)}%')
        if randint(1,perfect_breed)<breeding_points:
            bunker_breed = 'Бункер размножился'
    return chance_breed, bunker_breed


def survival(members, survival_points):
    bunker_alive = 'Бункер не выжил'
    chance_survive = 'Шанс выживания игроков в бункере 0 %' 
    if members.filter(alive=True).exists():
        chance_survive = (f'Шанс выживания игроков в бункере {round(survival_points/(55/100),1)}%')
        if randint(1,55)<survival_points:
            bunker_alive = 'Бункер выжил'
    return chance_survive, bunker_alive


def context(members,survival_points,breeding_points, logs):
    chance_survive, bunker_alive = survival(members=members, survival_points=survival_points)
    chance_breed, bunker_breed = reproduction(members=members, breeding_points=breeding_points, bunker_alive=bunker_alive)

    return {'breeding_points' : breeding_points, 
    'survival_points' : survival_points, 
    'members_alive':members.filter(alive=True), 
    'members_dead':members.filter(alive=False),
    'logs':logs,
    'chance_survive': chance_survive,
    'bunker_alive':bunker_alive,
    'chance_breed':chance_breed,
    'bunker_breed' :bunker_breed,
    }