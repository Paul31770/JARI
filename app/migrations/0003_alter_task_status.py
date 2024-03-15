# Generated by Django 4.2.11 on 2024-03-13 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('planned', 'Planned'), ('progress', 'In Progress'), ('completed', 'Completed'), ('validated', 'Validated'), ('paused', 'Paused')], default='paused', max_length=20),
        ),
    ]
