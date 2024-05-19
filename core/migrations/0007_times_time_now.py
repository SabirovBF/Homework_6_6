from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_times_text_now'),
    ]

    operations = [
        migrations.AddField(
            model_name='times',
            name='time_now',
            field=models.TextField(blank=True, verbose_name='Запись'),
        ),
    ]