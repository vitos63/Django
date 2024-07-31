from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import  CreateView
from .forms import FormMemberFactory, FormMember
from django.urls import reverse_lazy
from .models import MemberCharact

def index(request):
    if request.method =='POST':
        fields = ['sex', 'age', 'profession', 'health', 'hobbii', 'phobia', 'baggage', 'fact_1', 'fact_2']
        for i in range(4):
            form ={}
            for j in fields:
                if not request.POST[f'form-{i}-{j}']:
                    return render(request, 'bunker_app/ok.html')
                form[j] = request.POST[f'form-{i}-{j}']
            form = FormMember(form)
            if form.is_valid():
                form = form.save()
    else:
        form = FormMemberFactory()
    return render(request, 'bunker_app/index.html', {'form':form})
