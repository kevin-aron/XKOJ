# Generated by Django 3.2.8 on 2023-05-02 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0018_gamesubmission_private'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamerk',
            name='playersubs',
        ),
    ]
