from typing import Any
from django import forms
from .models import MemberCharact, Profession, Health, Hobbii, Phobia, Baggage, Fact, Disasters
from django.core.exceptions import ValidationError

class FormMember(forms.ModelForm):
    age = forms.IntegerField(label='Возраст', min_value=18,max_value=100)
    profession = forms.ModelChoiceField(queryset=Profession.objects.all(), label='Профессия', empty_label= 'Профессия не выбрана', required=False)
    health = forms.ModelChoiceField(queryset=Health.objects.all(), label='Здоровье', empty_label= 'Здоровье не выбрано', required=False)
    stage = forms.IntegerField(label='Стадия',min_value=0, max_value=100, step_size=10, required=False)
    hobbii = forms.ModelChoiceField(queryset = Hobbii.objects.all(), label = 'Хобби', empty_label = 'Хобби не выбрано', required=False)
    phobia = forms.ModelChoiceField(queryset = Phobia.objects.all(), label = 'Фобия', empty_label = 'Фобия не выбрана', required=False)
    baggage = forms.ModelChoiceField(queryset = Baggage.objects.all(), label = 'Багаж', empty_label = 'Багаж не выбран', required=False)
    fact_1 = forms.ModelChoiceField(queryset = Fact.objects.all(), label = 'Факт 1', empty_label = 'Факт не выбран', required=False)
    fact_2 = forms.ModelChoiceField(queryset = Fact.objects.all(), label = 'Факт 2', empty_label = 'Факт не выбран', required=False)

    class Meta:
        model = MemberCharact
        exclude = ['infection', 'alive']
    
    def clean(self):
        return super().clean()

class MembersCount(forms.Form):
    members_count = forms.IntegerField(label = 'Количество игроков прошедших в бункер',min_value=1, max_value=10)
    disaster = forms.ModelChoiceField(queryset=Disasters.objects.all(), label='Катастрофа', empty_label='Катастрофа не выбрана')

    def clean_members_count(self):
        members_count = self.cleaned_data['members_count']
        if 0<members_count<11:
            return members_count
        raise ValidationError('Количество игроков должно быть от 1 до 10')



