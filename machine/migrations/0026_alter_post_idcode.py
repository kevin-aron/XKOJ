# Generated by Django 3.2.8 on 2023-05-05 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0025_auto_20230505_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='idcode',
            field=models.SlugField(blank=True, max_length=20, unique=True, verbose_name='博客路径'),
        ),
    ]