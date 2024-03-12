from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def project(request, project_id):
    
    # Creation d'un projet pour tester
    project = Project.objects.get(pk=project_id)
    return render(request, 'project.html', {'project': project})

def liste_conges(request):
    conges = Conges.objects.all()
    return render(request, 'conges.html', {'conges': conges})