# Generated by Django 4.2.10 on 2024-03-12 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('paused', 'Paused'), ('planned', 'Planned'), ('progress', 'In Progress'), ('delivered', 'Delivered')], default='paused', max_length=20),
        ),
    ]
