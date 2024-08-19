from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import  CreateView
from .forms import FormMemberFactory, FormMember
from django.urls import reverse_lazy,reverse
from .models import MemberCharact
from .utils import total_score

def index(request):
    if request.method =='POST':
        fields = ['name', 'sex', 'age', 'profession', 'health', 'stage', 'hobbii', 'phobia', 'baggage', 'fact_1', 'fact_2']
        for i in range(4):
            form ={}
            for j in fields:
                if not request.POST[f'form-{i}-{j}']:
                    return redirect(reverse('calculat'))
                form[j] = request.POST[f'form-{i}-{j}']
            form = FormMember(form)
            if form.is_valid():
                form = form.save()
        return redirect(reverse('calculat'))
    else:
        form = FormMemberFactory()
    return render(request, 'bunker_app/index.html', {'form':form})


def calculation(request):
    members = MemberCharact.objects.all()
    breeding_points, survival_points = total_score(members)
    breeding_points /= members.all().count()
    survival_points /= members.all().count()
    return render(request, 'bunker_app/calculation.html', {'breeding_points' : breeding_points, 
    'survival_points' : survival_points, 
    'members_alive':members.filter(alive=True), 
    'members_dead':members.filter(alive=False)})

def clean_database(request):
    MemberCharact.objects.all().delete()
    return redirect(reverse('home'))



