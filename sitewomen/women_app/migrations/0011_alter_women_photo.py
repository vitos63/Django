# Generated by Django 5.0.7 on 2024-07-22 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women_app', '0010_alter_category_options_alter_women_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото'),
        ),
    ]
