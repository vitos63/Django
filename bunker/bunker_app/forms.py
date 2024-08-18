from django import forms
from .models import MemberCharact, Profession, Health, Hobbii, Phobia, Baggage, Fact
from django.forms import formset_factory

class FormMember(forms.ModelForm):
    profession = forms.ModelChoiceField(queryset=Profession.objects.all(), label='Профессия', empty_label= 'Профессия не выбрана')
    health = forms.ModelChoiceField(queryset=Health.objects.all(), label='Здоровье', empty_label= 'Здоровье не выбрано')
    hobbii = forms.ModelChoiceField(queryset = Hobbii.objects.all(), label = 'Хобби', empty_label = 'Хобби не выбрано')
    phobia = forms.ModelChoiceField(queryset = Phobia.objects.all(), label = 'Фобия', empty_label = 'Фобия не выбрана')
    baggage = forms.ModelChoiceField(queryset = Baggage.objects.all(), label = 'Багаж', empty_label = 'Багаж не выбран')
    fact_1 = forms.ModelChoiceField(queryset = Fact.objects.all(), label = 'Факт 1', empty_label = 'Факт не выбран')
    fact_2 = forms.ModelChoiceField(queryset = Fact.objects.all(), label = 'Факт 2', empty_label = 'Факт не выбран')

    class Meta:
        model = MemberCharact
        exclude = ['infection', 'alive']


FormMemberFactory = formset_factory(FormMember, extra = 4)
