# Generated by Django 3.2.8 on 2023-05-05 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0027_remove_post_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='idcode',
            field=models.SlugField(blank=True, unique=True, verbose_name='博客路径'),
        ),
    ]
