# Generated by Django 3.2.8 on 2023-04-22 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0012_auto_20230423_0458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='code',
        ),
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.URLField(default=-1, verbose_name='博客链接'),
        ),
    ]
