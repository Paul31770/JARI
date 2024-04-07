from django.shortcuts import render, redirect, get_object_or_404
from app.models import *
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from app.forms import ProjectForm, TaskForm
from django.shortcuts import redirect
from django.http import JsonResponse
from django.db import connection

def drag_drop(request, project_id):
    progress=[]
    paused=[]
    completed=[]
    validated=[]
    planned=[]
    all_status = {'planned': [], "progress": [], "completed": [], "paused": [], "validated": []}
    try:
        project = Project.objects.get(id=project_id)
        all_name = Task.objects.filter(project=project)
        
        for task in all_name:
            if task.status == "progress":
                all_status['progress'].append(task)
            elif task.status == "paused":
                all_status['paused'].append(task)
            elif task.status == "completed":
                all_status['completed'].append(task)
            elif task.status == "validated":
                all_status['validated'].append(task)
            elif task.status == "planned":
                all_status['planned'].append(task)
    except Project.DoesNotExist:
        project = None
    return ({'all_status': all_status})

def update_task_advancement(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        new_advancement = request.POST.get('new_value')
        
        try:
            task = Task.objects.get(id=task_id)
            task.advancement = new_advancement
            task.save()
            return JsonResponse({'success': True})
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task does not exist'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def supprTask(request):
    task_id = request.GET.get('task_id')
    print("TASK ID:", task_id)
    
def update_task_status(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        new_status = request.POST.get('new_status')
        print("TASK id ", task_id)
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM app_task WHERE title= %s", [task_id])
                rows = cursor.fetchall()
                for row in rows:
                    task_idd=row[0]
            task = Task.objects.get(id=task_idd)
            task.status = new_status
            task.save()
            return JsonResponse({'success': True})
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task does not exist'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
from .forms import *


def index(request):
    return HttpResponse("Home page")

def project(request, project_id):
    context=drag_drop(request, project_id)
    all_status=context.get("all_status",[])
    progress=context.get("progress",[])
    paused=context.get("paused",[])
    completed=context.get("completed",[])
    validated=context.get("validated",[])
    planned=context.get("planned",[])
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return render(request, '404.html', {'message': 'Project not found'})
    
    return render(request, 'projects/project.html', {'all_status':all_status, 'project': project, 'progress': progress, 'paused': paused, 'completed': completed, 'validated': validated, 'planned': planned})

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

def liste_conges(request):
    conges = Conges.objects.all()
    return render(request, 'conges.html', {'conges': conges})

def ajout_conges(request):
    if request.method == 'POST':
        form = CongesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_conges')
    else:
        form = CongesForm()
    return render(request, 'ajouter_conges.html', {'form': form})

def supprimer_conge(request, conge_id):
    conge = get_object_or_404(Conges, id=conge_id)
    conge.delete()

    return redirect('liste_conges')