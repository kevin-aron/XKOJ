# Generated by Django 3.2.8 on 2023-04-30 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0016_auto_20230428_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamesubmission',
            name='idnum',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='gamesubmission',
            name='idcode',
            field=models.CharField(default='xxx', max_length=100, unique=True),
        ),
    ]