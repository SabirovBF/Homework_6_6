# Generated by Django 5.0.6 on 2024-05-18 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_times_time_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='times',
            name='time_now',
            field=models.DateTimeField(),
        ),
    ]
