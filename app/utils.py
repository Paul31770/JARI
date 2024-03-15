import datetime
from app.models import Project, Task

# On update l'avancement du projet en fonction de l'avancement des taches
def update_project_advancement(project_id):
    project = Project.objects.get(id=project_id)
    tasks = project.task_set.all()
    total_advancement = 0
    for task in tasks:
        total_advancement += task.advancement
    project.advancement = total_advancement / len(tasks)
    project.save()

# Si la start_date d'une tache est passée et qu'elle est en planned ou in_progress: projet en in_progress
# Si les taches sont toutes paused: projet en paused
# Si les toutes les taches sont soit dans completed soit dans validated: projet en delivered
def update_project_status(project_id):
    project = Project.objects.get(id=project_id)
    tasks = project.task_set.all()

    if len(tasks) == 0:
        project.status = 'paused'
        project.save()
        return
    
    for task in tasks:
        if task.status == 'planned' or task.status == 'in_progress':
            if task.start_date <= datetime.date.today():
                project.status = 'in_progress'
                project.save()
                return
            
    paused_count = 0
    completed_count = 0
    for task in tasks:
        if task.status == 'paused':
            paused_count += 1
        
        if task.status == 'completed' or task.status == 'validated':
            completed_count += 1

    if paused_count == len(tasks):
        project.status = 'paused'
        project.save()
        return
    
    if completed_count == len(tasks):
        project.status = 'delivered'
        project.save()
        return
    
    print(paused_count)
    print(completed_count)
    print(len(tasks))

    project.save()
