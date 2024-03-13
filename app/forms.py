from django import forms
from .models import Project, Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'start_date', 'delivery_date', 'manager']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'delivery_date': forms.DateInput(attrs={'type': 'date'}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'start_date', 'priority', 'est_days']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            # priority is a number field between 1 and 3
            'priority': forms.NumberInput(attrs={'type': 'number', 'min': 1, 'max': 3}),
        }