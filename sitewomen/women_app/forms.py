from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from .models import Category, Husband, TagPost, Women
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label='Категории', empty_label='Категория не выбрана')
    husband = forms.ModelChoiceField(Husband.objects.filter(wuman__husband__isnull=True), required=False, label='Муж', empty_label='Муж не выбран')

    class Meta:
        model = Women
        fields = ['title', 'content', 'is_published', 'cat', 'husband', 'tags', 'photo']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-input'}),
            'content' : forms.Textarea(attrs={'cols':50, 'rows':5})
                   }
        labels = {'slug' : 'URL'}

    def clean_title(self) :
        title = self.cleaned_data['title']
        ALLOWED_CHARS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789- '
        if not (set(title)<= set(ALLOWED_CHARS)):
            raise ValidationError('Заголовок должен состоять из русских букв')
        return title


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя',  widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='E-mail',widget=forms.TextInput(attrs={'class': 'form-input'}))
    content = forms.CharField(label='Комментарии', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()

    def __init__(self,*args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields['name'].initial = user.username
            self.fields['name'].widget.attrs['readonly'] = True

            if user.email:
                self.fields['email'].initial = user.email
                self.fields['email'].widget.attrs['readonly'] = True
        