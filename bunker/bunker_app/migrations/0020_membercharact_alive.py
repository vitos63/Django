# Generated by Django 5.1 on 2024-08-14 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bunker_app', '0019_membercharact_infection'),
    ]

    operations = [
        migrations.AddField(
            model_name='membercharact',
            name='alive',
            field=models.BooleanField(default=True, verbose_name='Живой'),
        ),
    ]
