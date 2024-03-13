from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

def drag_drop(request):
    # Item.objects.create(name='CCS', column='column1')
    # Item.objects.create(name='TARZ', column='column2')
    all_items = Item.objects.all()
    all_name= Task.objects.all()
    print("all items ", all_items)
    print("all name ",all_name)
    return render(request, 'drag.html',  context={'all_items': all_items, 'all_name': all_name})

def index(request):
    return HttpResponse("Home page")

def project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return render(request, '404.html', {'message': 'Project not found'})
    
    return render(request, 'project.html', {'project': project})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})
    
def create_project(request):
        return HttpResponse("Create project")
