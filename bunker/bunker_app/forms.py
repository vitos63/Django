from django import forms
from .models import MemberCharact
from django.forms import formset_factory

class FormMember(forms.ModelForm):
    class Meta:
        model = MemberCharact
        fields = '__all__'

FormMemberFactory = formset_factory(FormMember, extra = 4)