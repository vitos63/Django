# Generated by Django 5.1 on 2024-08-18 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bunker_app', '0026_rename_survive_points_membercharact_survival_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membercharact',
            name='breeding_points',
        ),
        migrations.RemoveField(
            model_name='membercharact',
            name='survival_points',
        ),
    ]