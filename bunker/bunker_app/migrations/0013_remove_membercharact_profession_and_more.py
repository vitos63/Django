# Generated by Django 5.1 on 2024-08-12 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bunker_app', '0012_rename_baggage_baggage_baggage_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membercharact',
            name='profession',
        ),
        migrations.AddField(
            model_name='membercharact',
            name='profession',
            field=models.ManyToManyField(max_length=100, null=True, related_name='profession', to='bunker_app.profession', verbose_name='Профессия'),
        ),
    ]
