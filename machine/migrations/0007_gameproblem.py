# Generated by Django 3.2.8 on 2023-04-25 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0006_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameProblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine.game')),
                ('problem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='machine.problem')),
            ],
        ),
    ]
