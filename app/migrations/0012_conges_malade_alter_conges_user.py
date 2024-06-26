# Generated by Django 4.2.9 on 2024-03-15 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_merge_20240314_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='conges',
            name='malade',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='conges',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='app.user'),
        ),
    ]
