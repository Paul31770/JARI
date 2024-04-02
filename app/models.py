from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Project(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('paused', 'Paused'),
        ('planned', 'Planned'),
        ('progress', 'In Progress'),
        ('delivered', 'Delivered'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='paused')
    advancement = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    STATUS_CHOICES = (
        ('planned', 'Planned'),
        ('progress', 'In Progress'),
        ('completed', 'Completed'),
        ('validated', 'Validated'),
        ('paused', 'Paused'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='paused')
    start_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField()
    est_days = models.IntegerField()
    advancement = models.IntegerField(default=0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_tasks')
    assigned_users = models.ManyToManyField(User, blank=True, related_name='asigned_tasks', verbose_name='Asigned users')
    subtasks = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='parent_tasks', verbose_name='Subtasks')
    required_tasks = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='dependent_tasks', verbose_name='Required tasks')

    def __str__(self):
        return self.title

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