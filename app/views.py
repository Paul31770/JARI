from django.shortcuts import render
from app.models import *
# Create your views here.
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
            
            
            
    
    # print("a ",Task.objects)
    # print("all name ",all_name)
    return render(request, 'drag.html',  context={'progress': progress,'paused': paused,'completed': completed,'validated': validated,'planned': planned})

    
from django.http import HttpResponse, Http404
from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    
    return render(request, 'project.html', {'project': project})
