# Generated by Django 5.0.7 on 2024-07-23 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0006_alter_games_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='points',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]