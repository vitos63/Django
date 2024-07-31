from django import forms
from .models import Category, Husband, TagPost, Women
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core.exceptions import ValidationError


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
    
class UploadFileForm(forms.Form):
    file = forms.FileField(label='Файл')