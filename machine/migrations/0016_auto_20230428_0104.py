# Generated by Django 3.2.8 on 2023-04-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0015_rename_totaltime_gamesubmission_nowtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamesubmission',
            name='idcode',
            field=models.CharField(default='xxxaxxx', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='gamesubmission',
            name='link',
            field=models.URLField(default=-1),
        ),
        migrations.AddField(
            model_name='submission',
            name='idcode',
            field=models.CharField(default='xxxaxxx', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='link',
            field=models.URLField(default=-1),
        ),
    ]