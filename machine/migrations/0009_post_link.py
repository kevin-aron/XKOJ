# Generated by Django 3.2.8 on 2023-04-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0008_post_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.URLField(default=-1, verbose_name='问题链接'),
        ),
    ]