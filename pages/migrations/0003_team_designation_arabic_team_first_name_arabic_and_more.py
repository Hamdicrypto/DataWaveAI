# Generated by Django 5.1.1 on 2024-10-27 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_teams_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='designation_arabic',
            field=models.CharField(default=models.CharField(max_length=100), max_length=100),
        ),
        migrations.AddField(
            model_name='team',
            name='first_name_arabic',
            field=models.CharField(default=models.CharField(max_length=100), max_length=100),
        ),
        migrations.AddField(
            model_name='team',
            name='last_name_arabic',
            field=models.CharField(default=models.CharField(max_length=100), max_length=100),
        ),
    ]
