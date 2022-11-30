from django import forms

from news.models import Category

attrs = {'class': 'form-control'}


class NewsForm(forms.Form):
    title = forms.CharField(label="Наименование", max_length=150, widget=forms.TextInput(attrs=attrs))
    content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5
    }))
    is_published = forms.BooleanField(label='Опубликовно', initial=True)
    category = forms.ModelChoiceField(label='Категория', empty_label="Chose the category",
                                      queryset=Category.objects.all(), widget=forms.Select(attrs=attrs))
