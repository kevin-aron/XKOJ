# Generated by Django 3.2.8 on 2023-04-25 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0022_delete_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gamename', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('link', models.URLField(blank=True, max_length=256)),
                ('timestart', models.DateTimeField(default=0)),
                ('timeend', models.DateTimeField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('gamestatement', models.TextField(default=0)),
                ('gamehard', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='GameSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('result', models.CharField(max_length=20)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine.game')),
                ('problem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='machine.problem')),
                ('submitter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='machine.coder')),
            ],
        ),
        migrations.CreateModel(
            name='GameProblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine.game')),
                ('problem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='machine.problem')),
            ],
        ),
    ]
