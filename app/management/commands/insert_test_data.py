from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = 'Insert test data into the database'

    def handle(self, *args, **kwargs):
      User = apps.get_model('app', 'User')
      Project = apps.get_model('app', 'Project')
      Task = apps.get_model('app', 'Task')
      Role = apps.get_model('app', 'Role')
      Permission = apps.get_model('app', 'Permission')
      UserProject = apps.get_model('app', 'UserProject')
      UserRole = apps.get_model('app', 'UserRole')
      RolePermission = apps.get_model('app', 'RolePermission')

      # Deleting all data
      User.objects.all().delete()
      Project.objects.all().delete()
      Task.objects.all().delete()
      Role.objects.all().delete()
      Permission.objects.all().delete()
      UserProject.objects.all().delete()
      UserRole.objects.all().delete()
      RolePermission.objects.all().delete()

      # Creation d'un utilisateur pour tester
      user = User(username="User1")
      user.save()

      # Creation d'un projet pour tester
      project = Project(title="Création d'une site e-commerce", start_date="2024-03-10", delivery_date="2024-04-12", manager=user)
      project.save()

      project2 = Project(title="Projet de test 1", start_date="2024-01-12", delivery_date="2025-03-12", manager=user)
      project2.save()

      project3 = Project(title="Projet test 2", start_date="2024-01-12", delivery_date="2025-03-12", manager=user)
      project3.save()

      project4 = Project(title="Projet sans contenu 3", start_date="2024-01-12", delivery_date="2025-03-12", manager=user)
      project4.save()

      # Creation d'une tache pour tester
      task1 = Task(title="Création de la page de login", description="Créer la page de login ainsi que tous ses composants UI", status="progress", start_date="2024-03-12", priority=2, advancement=34, project=project, est_days=1, manager=user)
      task1.save()

      task2 = Task(title="Création de la base de données", description="Créer la base de donnée ainsi que toutes ses tables, relations et y ajouter les données de test", status="paused", start_date="2024-03-12", priority=3, advancement=13, project=project, est_days=2,manager=user)
      task2.save()

      task3 = Task(title="Réaliser l'interface utilisateur", description="Réalisation du fronted de l'app", status="progress", start_date="2024-03-12", priority=2, advancement=78, project=project, est_days=5, manager=user)
      task3.save()

      task4 = Task(title="Faire le diagramme de la BDD", description="Afin de pouvoir créer notre base de donnée il est nécéssaire de réaliser en amont un diagramme", status="validated", start_date="2024-03-12", priority=2, advancement=100, project=project, est_days=2, manager=user)
      task4.save()

      task5 = Task(title="Deployer l'API dans le cloud azure", description="Il est demandé de paramétrer le cloud azure pour y déployer l'application", status="planned", start_date="2024-03-19", priority=2, advancement=0, project=project, est_days=4, manager=user)
      task5.save()
      
      task6 = Task(title="task six", description="test", status="planned", start_date="2024-03-12", priority=1, advancement=1, project=project, est_days=1, manager=user)
      task6.save()

      # Creation d'un role pour tester
      role = Role(name="testRole")
      role.save()

      # Creation d'une permission pour tester
      permission = Permission(name="testPermission")
      permission.save()

      # Creation d'une relation entre un utilisateur et un projet pour tester
      userproject = UserProject(user=user, project=project)
      userproject.save()

      # Creation d'une relation entre un utilisateur et un role pour tester
      userrole = UserRole(user=user, role=role)
      userrole.save()

      # Creation d'une relation entre un role et une permission pour tester
      rolepermission = RolePermission(role=role, permission=permission)
      rolepermission.save()

      self.stdout.write(self.style.SUCCESS('Test data inserted successfully'))