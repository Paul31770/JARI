from django.shortcuts import render
from .models import Conges

# Create your views here.

def liste_conges(request):
    conges = Conges.objects.all()
    return render(request, 'conges.html', {'conges': conges})