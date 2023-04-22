# Generated by Django 3.2.8 on 2023-04-22 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0006_submission_ac_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '博客集',
                'verbose_name_plural': '博客集',
            },
        ),
    ]