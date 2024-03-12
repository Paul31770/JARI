from django.shortcuts import render
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
