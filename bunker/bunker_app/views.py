from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import  CreateView
from .forms import FormMember, MembersCount
from django.urls import reverse_lazy,reverse
from .models import MemberCharact, Disasters
from .utils import total_score
from django.forms import formset_factory
from random import randint


def index(request):
    if request.method=='POST':
        form = MembersCount(request.POST)
        if form.is_valid():
            members_count = form.cleaned_data['members_count']
            disaster = Disasters.objects.get(disaster_ru=form.cleaned_data['disaster']).slug
            return redirect(reverse_lazy('members_forms',kwargs= {'members_count':members_count, 'disaster':disaster}))
    else:
        form = MembersCount()
    return render(request, 'bunker_app/index.html', {'form':form})



def members_forms(request, members_count,disaster):
    MemberCharact.objects.all().delete()
    FormMemberFactory = formset_factory(FormMember, extra = members_count)
    if request.method =='POST':
        fields = ['name', 'sex', 'age', 'profession', 'health', 'stage', 'hobbii', 'phobia', 'baggage', 'fact_1', 'fact_2']
        for i in range(members_count):
            form ={}
            for j in fields:
                form[j] = request.POST[f'form-{i}-{j}']
            form = FormMember(form)
            if form.is_valid():
                form = form.save()
        return redirect(reverse('calculat', kwargs={'disaster':disaster}))
    else:
        form = FormMemberFactory()
    return render(request, 'bunker_app/members_forms.html', {'form':form})


def calculation(request, disaster):
    disaster = Disasters.objects.get(slug=disaster).disaster_ru
    logs = []
    members = MemberCharact.objects.all()
    breeding_points, survival_points, logs = total_score(members, logs, disaster)
    breeding_points /= members.all().count()
    survival_points /= members.all().count()
    chance = ''
    bunker_alive = 'Бункер не выжил'
    if members.filter(alive=True).exists():
        chance = (f'Шанс выживания игроков в бункере {round(survival_points/(55/100),1)}%')
        if randint(1,55)<survival_points:
            bunker_alive = 'Бункер выжил'
    return render(request, 'bunker_app/calculation.html', {'breeding_points' : breeding_points, 
    'survival_points' : survival_points, 
    'members_alive':members.filter(alive=True), 
    'members_dead':members.filter(alive=False),
    'logs':logs,
    'chance': chance,
    'bunker_alive':bunker_alive
    })


