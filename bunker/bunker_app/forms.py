from typing import Any
from django import forms
from .models import MemberCharact, Profession, Health, Hobbii, Phobia, Baggage, Fact, Disasters
from django.core.exceptions import ValidationError


class FormMember(forms.ModelForm):
    age = forms.IntegerField(label='Возраст', min_value=18,max_value=100, required=True, widget=forms.NumberInput(attrs={'required':'required'}))
    profession = forms.ModelChoiceField(queryset=Profession.objects.all(), label='Профессия', empty_label= 'Профессия не выбрана', required=True, widget=forms.Select(attrs={'required':'requred'}))
    health = forms.ModelChoiceField(queryset=Health.objects.all(), label='Здоровье', empty_label= 'Здоровье не выбрано', required=True, widget=forms.Select(attrs={'required':'requred'}))
    stage = forms.IntegerField(label='Стадия',min_value=0, max_value=100, step_size=10, required=True, widget=forms.NumberInput(attrs={'required':'required'}))
    hobbii = forms.ModelChoiceField(queryset= Hobbii.objects.all(), label = 'Хобби', empty_label = 'Хобби не выбрано', required=True,  widget=forms.Select(attrs={'required':'requred'}))
    phobia = forms.ModelChoiceField(queryset = Phobia.objects.all(), label = 'Фобия', empty_label = 'Фобия не выбрана', required=True,  widget=forms.Select(attrs={'required':'requred'}))
    baggage = forms.ModelChoiceField(queryset =Baggage.objects.all(), label = 'Багаж', empty_label = 'Багаж не выбран', required=True,  widget=forms.Select(attrs={'required':'requred'}))
    fact_1 = forms.ModelChoiceField(queryset = Fact.objects.all(), label = 'Факт 1', empty_label = 'Факт не выбран', required=True,  widget=forms.Select(attrs={'required':'requred'}))
    fact_2 = forms.ModelChoiceField(queryset = Fact.objects.all(), label = 'Факт 2', empty_label = 'Факт не выбран', required=True,  widget=forms.Select(attrs={'required':'requred'}))

    class Meta:
    
        model = MemberCharact
        fields = ['name', 'sex', 'age', 'profession', 'health', 'stage', 'hobbii', 'phobia', 'baggage', 'fact_1', 'fact_2']
        widgets = {
            'name':forms.TextInput(attrs={'required':'requred'}),
            'sex':forms.Select(attrs={'required':'requred'}),
            }
        

class MembersCount(forms.Form):
    members_count = forms.IntegerField(label = 'Количество игроков прошедших в бункер',min_value=1, max_value=10)
    disaster = forms.ModelChoiceField(queryset=Disasters.objects.all(), label='Катастрофа', empty_label='Катастрофа не выбрана')

    def clean_members_count(self):
        members_count = self.cleaned_data['members_count']
        if 0<members_count<11:
            return members_count
        raise ValidationError('Количество игроков должно быть от 1 до 10')
    

class RequiredFormSet(forms.BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False