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
      RequiredTask = apps.get_model('app', 'RequiredTask')
      TaskSubtask = apps.get_model('app', 'TaskSubtask')

      # Deleting all data
      User.objects.all().delete()
      Project.objects.all().delete()
      Task.objects.all().delete()
      Role.objects.all().delete()
      Permission.objects.all().delete()
      UserProject.objects.all().delete()
      UserRole.objects.all().delete()
      RolePermission.objects.all().delete()
      RequiredTask.objects.all().delete()
      TaskSubtask.objects.all().delete()

      # Creation d'un utilisateur pour tester
      user = User(username="User1")
      user.save()

      # Creation d'un projet pour tester
      project = Project(title="Project One.", start_date="2024-03-12", delivery_date="2024-03-12", manager=user)
      project.save()

      # Creation d'une tache pour tester
      task1 = Task(title="task one", description="test", status="in_progress", start_date="2024-03-12", priority=1, advancement=1, project=project)
      task1.save()

      task2 = Task(title="task two", description="test", status="paused", start_date="2024-03-12", priority=1, advancement=1, project=project)
      task2.save()

      task3 = Task(title="task three", description="test", status="completed", start_date="2024-03-12", priority=1, advancement=1, project=project)
      task3.save()

      task4 = Task(title="task four", description="test", status="validated", start_date="2024-03-12", priority=1, advancement=1, project=project)
      task4.save()

      task5 = Task(title="task five", description="test", status="planned", start_date="2024-03-12", priority=1, advancement=1, project=project)
      task5.save()

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

      # Creation d'une tache requise pour tester
      requiredtask = RequiredTask(task=task2, required_task=task4)
      requiredtask.save()

      # Creation d'une sous-tache pour tester
      tasksubtask = TaskSubtask(task=task3, subtask=task1)
      tasksubtask.save()

      self.stdout.write(self.style.SUCCESS('Test data inserted successfully'))