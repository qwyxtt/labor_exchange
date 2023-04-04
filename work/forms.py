from django import forms
from .models import Task

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['owner', 'executor']

    end_date = forms.DateField(widget=forms.SelectDateWidget())
