# Generated by Django 3.0.7 on 2020-08-24 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0003_auto_20200821_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='callofroll',
            name='cursus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lycee.Cursus'),
        ),
        migrations.AlterField(
            model_name='callofroll',
            name='date',
            field=models.DateField(help_text='missing date', max_length=255, null=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='callofroll',
            name='endTime',
            field=models.CharField(help_text='End Time of lesson', max_length=255, null=True, verbose_name='End Time'),
        ),
        migrations.AlterField(
            model_name='callofroll',
            name='isPresent',
            field=models.BooleanField(verbose_name='Present'),
        ),
        migrations.AlterField(
            model_name='callofroll',
            name='startTime',
            field=models.TimeField(help_text='Start Time of lesson', max_length=255, null=True, verbose_name='Start Time'),
        ),
    ]