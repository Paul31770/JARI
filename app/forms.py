from django import forms
from .models import Project, Task, Conges, User

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

class LoginForm(forms.ModelForm):
    class Meta:
        model = User #rajouter password dans db
        fields = ['username', 'password']
        widgets = {
            'password' : forms.PasswordInput()
        }