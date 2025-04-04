# Generated by Django 5.1.7 on 2025-04-02 07:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='task_name',
            field=models.CharField(max_length=200, unique=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
        migrations.AlterField(
            model_name='todo',
            name='task_progress',
            field=models.CharField(choices=[('Pending', 'Pending'), ('InProgress', 'InProgress'), ('Completed', 'Completed')], max_length=300),
        ),
    ]
