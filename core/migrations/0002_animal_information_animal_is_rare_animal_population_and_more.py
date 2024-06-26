# Generated by Django 5.0.6 on 2024-05-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='information',
            field=models.TextField(blank=True, verbose_name='Информация'),
        ),
        migrations.AddField(
            model_name='animal',
            name='is_rare',
            field=models.BooleanField(default=False, verbose_name='Вымерающие животные'),
        ),
        migrations.AddField(
            model_name='animal',
            name='population',
            field=models.PositiveIntegerField(default=False, verbose_name='Популяция'),
        ),
        migrations.AddField(
            model_name='animal',
            name='type',
            field=models.CharField(choices=[('mammal', 'Млекопитающее'), ('fish', 'Рыба'), ('reptile', 'Рептилия')], default=0, max_length=100, verbose_name='Род'),
        ),
    ]
