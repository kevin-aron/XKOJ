# Generated by Django 3.2.8 on 2023-04-27 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0010_game_gamenum'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameproblem',
            name='passnum',
            field=models.IntegerField(default=0),
        ),
    ]
