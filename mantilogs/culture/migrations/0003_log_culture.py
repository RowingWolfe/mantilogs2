# Generated by Django 3.1 on 2020-10-15 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('culture', '0002_auto_20201015_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='culture',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='culture.culture'),
        ),
    ]
