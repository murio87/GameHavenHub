# Generated by Django 4.2.10 on 2024-08-28 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamerz', '0003_event_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='poster',
        ),
    ]
