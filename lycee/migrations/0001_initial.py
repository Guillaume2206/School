# Generated by Django 3.0.7 on 2020-07-06 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='aucun', max_length=50, null=True)),
                ('year_from_bac', models.SmallIntegerField(default=0, help_text='year since le bac', null=True, verbose_name='year')),
                ('scholar_year', models.CharField(default='0000-00001', max_length=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(null=True, verbose_name='date of birth')),
                ('last_name', models.CharField(default='???', help_text='last name of the student', max_length=255, verbose_name='lastname')),
                ('phone', models.CharField(default='0999999999', help_text='phone number of the student', max_length=10, verbose_name='phonenumber')),
                ('email', models.EmailField(default='x@y.z', help_text='phone number of the student', max_length=255, verbose_name='email')),
                ('comments', models.CharField(blank=True, default='', help_text='some comments about the student', max_length=255, verbose_name='comments')),
                ('cursus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lycee.Cursus')),
            ],
        ),
    ]
