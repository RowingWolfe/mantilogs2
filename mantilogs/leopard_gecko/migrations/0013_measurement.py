# Generated by Django 3.1.2 on 2020-10-30 00:57

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('leopard_gecko', '0012_auto_20201027_0703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('length', models.FloatField(default=0.0, help_text='cm')),
                ('weight', models.FloatField(default=0.0, help_text='gm')),
                ('gecko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leopard_gecko.gecko')),
            ],
        ),
    ]
