from django import forms
from django.forms import ModelForm
from .models import Table


class TableForm(forms.Form):
    TITLE_COLUMN = "title"
    DATE_COLUMN = "date"
    COUNT_COLUMN = 'count'
    DISTANCE_COLUMN = 'distance'
    FILTERS = (
        (DATE_COLUMN, 'Дата'),
        (TITLE_COLUMN, 'Название'),
        (COUNT_COLUMN, 'Количество'),
        (DISTANCE_COLUMN, 'Дистанция'),
    )
    a = forms.ChoiceField(choices=FILTERS)
