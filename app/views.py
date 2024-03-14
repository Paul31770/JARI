from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from .forms import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def project(request, project_id):
    
    # Creation d'un projet pour tester
    project = Project.objects.get(pk=project_id)
    return render(request, 'project.html', {'project': project})

def liste_conges(request):
    conges = Conges.objects.all()
    return render(request, 'conges.html', {'conges': conges})

def ajout_conges(request):
    if request.method == 'POST':
        date_debut = request.POST.get('date_debut')
        date_fin = request.POST.get('date_fin')
        user_id = request.POST.get('user_id')
        
        user = get_object_or_404(User, pk=user_id)
        nouveau_conges = Conges(date_debut=date_debut, date_fin=date_fin, user=user)
        nouveau_conges.save()

        return redirect('liste_conges')
    else:
        conges = Conges.objects.all()
        return render(request, 'ajouter_conges.html', {'conges': conges})
    
def ajouter_donnees(request):
    if request.method == 'POST':
        form = Conges_form(request.POST)
        if form.is_valid():
            form.save()  # Enregistre les données dans la base de données
            return redirect('liste_conges')  # Redirige vers une page de confirmation
    else:
        form = Conges_form()
    return render(request, 'conges.html', {'form': form})