"""
URL configuration for Jari project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
from app import views


urlpatterns = [
    path('', index),
    path('project/<int:project_id>/', project, name='project'),
    path('admin/', admin.site.urls),
    path('projects/', projects, name='projects'),
    path('create_project/', create_project, name='create_project'),
    path('edit_project/<int:project_id>', edit_project, name='edit_project'),
    path('create_task/<int:project_id>', create_task, name='create_task'),
    path('edit_task/<int:task_id>', edit_task, name='edit_task'),
    path('update_task_status/', update_task_status, name='update_task_status'),
    path('conges/', views.liste_conges, name='liste_conges'),
    path('ajouter_conges/', views.ajout_conges, name='ajouter_conges'),
]
