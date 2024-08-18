# Generated by Django 5.1 on 2024-08-09 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bunker_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membercharact',
            name='profession',
            field=models.CharField(choices=[('Doctor', 'Доктор'), ('Engineer', 'Инженер'), ('Teacher', 'Учитель'), ('Cook', 'Повар'), ('Secretary', 'Секретарь')], max_length=250, null=True, verbose_name='Профессия'),
        ),
    ]