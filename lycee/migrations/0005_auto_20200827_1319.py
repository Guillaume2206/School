# Generated by Django 3.0.7 on 2020-08-27 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0004_auto_20200824_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='callofroll',
            name='endTime',
        ),
        migrations.RemoveField(
            model_name='callofroll',
            name='startTime',
        ),
    ]
