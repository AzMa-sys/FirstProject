from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.forms import Textarea
from django.template.defaultfilters import title
from django.utils.deconstruct import deconstructible
from prompt_toolkit.validation import ValidationError

from .models import Sport, Category, Avi


class AddFormPage(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='выберите категорию')
    avail = forms.ModelChoiceField(queryset=Avi.objects.all(), required=False, label='Наличие')

    class Meta:
        model = Sport
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat', 'avail', 'tags']
        labels = {'slug': 'URL'}
        widgets ={
            'content': forms.Textarea(attrs={'cols': 50, 'row': 5})
        }

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Файл')

