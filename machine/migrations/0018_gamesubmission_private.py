# Generated by Django 3.2.8 on 2023-05-02 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0017_auto_20230430_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamesubmission',
            name='private',
            field=models.BooleanField(default=True),
        ),
    ]
