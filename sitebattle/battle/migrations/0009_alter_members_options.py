# Generated by Django 5.0.7 on 2024-07-23 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0008_alter_members_points'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='members',
            options={'ordering': ['-points'], 'verbose_name': 'Участники', 'verbose_name_plural': 'Участники'},
        ),
    ]
