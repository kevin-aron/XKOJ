# Generated by Django 3.2.8 on 2023-04-25 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0017_gameproblem_gamesubmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameproblem',
            name='problem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='machine.problem'),
        ),
        migrations.AlterField(
            model_name='gamesubmission',
            name='problem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='machine.problem'),
        ),
    ]