from django import forms
from .models import TodoListItem
from todolist import settings
from datetime import datetime
from django.utils import timezone


class DateInput(forms.DateInput):
    input_type = 'date'




class DateForm(forms.Form):

    date = forms.DateTimeField(widget=DateInput,initial=datetime.now().strftime("%Y-%m-%d"))
