# Generated by Django 3.1 on 2020-10-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantis_profiles', '0011_auto_20201001_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment_log',
            name='temp',
            field=models.CharField(default='0', max_length=40),
        ),
    ]
