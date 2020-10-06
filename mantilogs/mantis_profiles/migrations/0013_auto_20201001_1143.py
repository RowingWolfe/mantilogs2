# Generated by Django 3.1 on 2020-10-01 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantis_profiles', '0012_auto_20201001_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment_log',
            name='humidity',
            field=models.CharField(default='0', max_length=250),
        ),
        migrations.AlterField(
            model_name='environment_log',
            name='location',
            field=models.CharField(default='Unspecified', max_length=250),
        ),
        migrations.AlterField(
            model_name='environment_log',
            name='notes',
            field=models.CharField(default='None', max_length=250),
        ),
        migrations.AlterField(
            model_name='environment_log',
            name='temp',
            field=models.CharField(default='0', max_length=250),
        ),
    ]
