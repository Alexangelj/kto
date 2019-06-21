from django import forms
from .models import Task

class TaskForm(forms.Form):
    class Meta:
        model = Task
        fields= ["task_name", 'description', 'completed', 'priority']

"""
    task_name = forms.CharField(label='Task', max_length=150)
"""