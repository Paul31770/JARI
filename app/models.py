from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)

class Project(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('paused', 'Paused'),
        ('planned', 'Planned'),
        ('in progress', 'In Progress'),
        ('delivered', 'Delivered'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='paused')

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    STATUS_CHOICES = (
        ('planned', 'Planned'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed'),
        ('validated', 'Validated'),
        ('paused', 'Paused'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='paused')
    start_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    advancement = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Role(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

class Permission(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

class UserProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

class RequiredTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='required_tasks')
    required_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='required_by_tasks')

class TaskSubtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    subtask = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='parent_task')
