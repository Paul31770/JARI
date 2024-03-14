from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from app.forms import ProjectForm, TaskForm
from django.shortcuts import redirect

def drag_drop(request):
    return render(request, 'drag.html')

def index(request):
    return HttpResponse("Home page")

def project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return render(request, '404.html', {'message': 'Project not found'})
    
    return render(request, 'projects/project.html', {'project': project})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})
    
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(projects)
    else:
        form = ProjectForm()
    return render(request, 'projects/createProject.html', {'form': form})

def edit_project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return render(request, '404.html', {'message': 'Project not found'})
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect(projects)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/createProject.html', {'form': form, 'project': project})

def create_task(request, project_id):
    if request.method == 'POST':
        form = TaskForm(request.POST, project_id=project_id)
        if form.is_valid():
            form.instance.project_id = project_id
            form.save()
            return redirect(project, project_id)
    else:
        form = TaskForm(project_id=project_id)
    return render(request, 'createTask.html', {'form': form})

def edit_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return render(request, '404.html', {'message': 'Task not found'})
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task, project_id=task.project_id)
        if form.is_valid():
            form.save()
            return redirect(project, task.project_id)
    else:
        form = TaskForm(instance=task, project_id=task.project_id)
    return render(request, 'createTask.html', {'form': form, 'task': task})

