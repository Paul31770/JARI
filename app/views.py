from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from app.forms import ProjectForm, TaskForm
from django.shortcuts import redirect

def drag_drop(request):
    progress=[]
    paused=[]
    completed=[]
    validated=[]
    planned=[]
    all_name= Task.objects.all()
    for i in range(len(all_name)):
        print("o ",all_name[i].status)
        if all_name[i].status=="in_progress":
            progress.append(all_name[i])
        elif all_name[i].status=="paused":
            paused.append(all_name[i])
        elif all_name[i].status=="completed":
            completed.append(all_name[i])
        elif all_name[i].status=="validated":
            validated.append(all_name[i])
        elif all_name[i].status=="planned":
            planned.append(all_name[i])
            
    return render(request, 'drag.html',  context={'progress': progress,'paused': paused,'completed': completed,'validated': validated,'planned': planned})

def update_task_status(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        new_status = request.POST.get('new_status')
        print("STATUS ",new_status)
    #     try:
    #         task = Task.objects.get(id=task_id)
    #         task.status = new_status
    #         task.save()
    #         return JsonResponse({'success': True})
    #     except Task.DoesNotExist:
    #         return JsonResponse({'success': False, 'error': 'Task does not exist'})
    # return JsonResponse({'success': False, 'error': 'Invalid request method'})

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

