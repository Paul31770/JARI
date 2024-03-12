from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        ('app', '0002_alter_project_status'),
    ]

    operations = [
        migrations.RunPython(insert_test_data),

    ]
