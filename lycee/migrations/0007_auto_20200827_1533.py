# Generated by Django 3.0.7 on 2020-08-27 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0006_auto_20200827_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='callofroll',
            name='afternoon',
        ),
        migrations.RemoveField(
            model_name='callofroll',
            name='morning',
        ),
        migrations.AddField(
            model_name='callofroll',
            name='dayhalf',
            field=models.CharField(choices=[('MORNING', 'Morning'), ('AFTERNOON', 'Afternoon')], default='1', max_length=9),
        ),
    ]
