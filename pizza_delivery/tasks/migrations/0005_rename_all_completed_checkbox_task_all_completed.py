# Generated by Django 4.2.13 on 2024-06-10 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_all_completed_checkbox'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='all_completed_checkbox',
            new_name='all_completed',
        ),
    ]
