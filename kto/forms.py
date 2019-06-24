from django.forms import ModelForm
from .models import Task
from django import forms

ACCEPTABLE_FORMATS = ['%Y-%m-%d',      # '2006-10-25'
                      '%m/%d/%Y',      # '10/25/2006'
                      '%m/%d/%y']      # '10/25/06'

class TaskForm(forms.ModelForm):
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)
    class Meta:
        model = Task
        fields = ['task_name', 'description', 'completed', 'priority']
    
class DateTimeForm(forms.Form):
    task_name = forms.CharField(required=False)
    description = forms.CharField(required=False)
    completed = forms.BooleanField(required=False)
    priority = forms.IntegerField(required=False)
    start_date = forms.DateTimeField(required=False, input_formats=ACCEPTABLE_FORMATS)
    end_date = forms.DateTimeField(required=False, input_formats=ACCEPTABLE_FORMATS)           # '10/25/06')
    class Meta:
        model = Task
        fields = [
            'start_date',
            'end_date',
        ]