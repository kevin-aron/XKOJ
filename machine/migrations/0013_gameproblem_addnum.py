# Generated by Django 3.2.8 on 2023-04-27 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0012_auto_20230427_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameproblem',
            name='addnum',
            field=models.IntegerField(default=1),
        ),
    ]
