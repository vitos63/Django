# Generated by Django 4.2.1 on 2024-06-17 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('discord', models.URLField(unique=True)),
            ],
        ),
    ]
