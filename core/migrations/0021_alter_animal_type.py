# Generated by Django 5.0.6 on 2024-05-19 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_delete_times'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='type',
            field=models.CharField(choices=[('mammal', 'Млекопитающее'), ('fish', 'Рыба'), ('reptile', 'Рептилия'), ('birds', 'Пернатые')], default='mammal', max_length=100, verbose_name='Род'),
        ),
    ]
