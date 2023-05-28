from django import forms
from .models import Task


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['owner', 'executor', 'is_active']

    end_date = forms.DateField(widget=forms.SelectDateWidget(attrs={"class": "end-date-select"}))
