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

    def __init__(self, *args, **kwargs):

        # On récupère le project_id
        project_id = kwargs.pop('project_id', None)
        super(TaskForm, self).__init__(*args, **kwargs)

        # On filtre les sous-tâches et les tâches requises pour qu'elles soient liées au même projet que la tâche courante
        if project_id:
            self.fields['subtasks'].queryset = Task.objects.filter(project_id=project_id)
            self.fields['required_tasks'].queryset = Task.objects.filter(project_id=project_id)

    class Meta:
        model = Task
        fields = ['title', 'description', 'start_date', 'priority', 'est_days', 'subtasks', 'required_tasks']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'priority': forms.NumberInput(attrs={'type': 'number', 'min': 1, 'max': 3}),
            'subtasks': forms.CheckboxSelectMultiple(),
            'required_tasks': forms.CheckboxSelectMultiple(),
        }