# Generated by Django 5.1 on 2024-08-18 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bunker_app', '0027_remove_membercharact_breeding_points_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='membercharact',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя игрока'),
        ),
    ]
