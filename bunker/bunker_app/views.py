from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import FormMember, MembersCount, RequiredFormSet
from django.urls import reverse_lazy,reverse
from .models import MemberCharact, Disasters, Characteristics, Rules, Information
from .utils import total_score, context
from django.forms import formset_factory
from random import randint
from django.views.generic import FormView



class Index(ListView):
    queryset = Information.objects.get(name='Бункер-элит')
    context_object_name = 'object_list'
    template_name = 'bunker_app/index.html'
    extra_context ={'title':'Бункер'}


class Rules(ListView):
    model = Rules
    context_object_name = 'rules'
    template_name = 'bunker_app/rules.html'
    extra_context = {'title':'Правила игры'}


class DescriptionCharacteristics(ListView):
    model = Characteristics
    context_object_name = 'characteristics'
    template_name = 'bunker_app/characteristics.html'
    extra_context ={'title':'Описание характеристик'}

class Feedback(ListView):
    queryset = Information.objects.get(name='Обратная связь')
    context_object_name = 'feedback'
    template_name = 'bunker_app/feedback.html'
    extra_context ={'title':'Обратная связь'}


class Count(FormView):
    form_class = MembersCount
    template_name = 'bunker_app/count_disaster.html'
    extra_context ={'title':'Количество игроков'}
    def form_valid(self, form):
        self.request.session['disaster'] = Disasters.objects.get(disaster_ru=form.cleaned_data['disaster']).disaster_ru
        self.request.session['members_count'] = form.cleaned_data['members_count']
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        self.success_url = reverse_lazy('members_forms')
        return super().get_success_url()


def members_forms(request): 
    request.session['user'] = 'user_key'
    MemberCharact.objects.filter(session_key = request.session.session_key).delete()
    FormMemberFactory = formset_factory(FormMember, formset = RequiredFormSet, extra = request.session['members_count'])
    
    if request.method == 'POST':
        formset = FormMemberFactory(request.POST)
        if formset.is_valid():
            for form in formset:
                member = form.save(commit=False)  
                member.session_key = request.session.session_key  
                member.save()  
        return redirect(reverse('calculat'))
    else:
        formset = FormMemberFactory()
    return render(request, 'bunker_app/members_forms.html', {'title': 'Характеристики игроков','formset':formset})


def calculation(request):
    disaster = request.session['disaster']
    members = MemberCharact.objects.filter(session_key = request.session.session_key)
    breeding_points, survival_points, logs = total_score(members=members, disaster=disaster)
    data = context(members=members, survival_points=survival_points, breeding_points=breeding_points, logs=logs)
    data['title'] = 'Итоги игры'

    return render(request, 'bunker_app/calculation.html',context=data)


