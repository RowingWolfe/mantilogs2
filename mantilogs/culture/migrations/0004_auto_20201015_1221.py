# Generated by Django 3.1 on 2020-10-15 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culture', '0003_log_culture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quarantine',
            name='end_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
