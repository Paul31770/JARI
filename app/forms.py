from django import forms
from .models import Project, Task, Conges

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
        # Récupérer l'ID du projet
        project_id = kwargs.pop('project_id', None)
        super(TaskForm, self).__init__(*args, **kwargs)

        # Filtrer les sous-tâches et les tâches requises pour qu'elles soient liées au même projet que la tâche courante
        if project_id:
            self.fields['subtasks'].queryset = Task.objects.filter(project_id=project_id)
            self.fields['required_tasks'].queryset = Task.objects.filter(project_id=project_id)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")
        start_date = cleaned_data.get("start_date")
        priority = cleaned_data.get("priority")
        est_days = cleaned_data.get("est_days")
        
        # Si l'une des informations requises est manquante, définir la tâche comme étant en état "paused"
        if not (start_date and priority and est_days):
            cleaned_data['status'] = 'paused'
        
        return cleaned_data

    class Meta:
        model = Task
        fields = ['title', 'description', 'start_date', 'priority', 'est_days', 'manager', 'assigned_users', 'subtasks', 'required_tasks']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'priority': forms.NumberInput(attrs={'type': 'number', 'min': 1, 'max': 3}),
            'subtasks': forms.CheckboxSelectMultiple(),
            'required_tasks': forms.CheckboxSelectMultiple(),
            'manager': forms.RadioSelect(),
            'assigned_users': forms.CheckboxSelectMultiple(),
        }
class CongesForm(forms.ModelForm):
    malade = forms.ChoiceField(choices=[(False, 'Non'), (True, 'Oui')], initial=False)
    class Meta:
        model = Conges
        fields = ['date_debut', 'date_fin', 'user', 'malade']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
        }
