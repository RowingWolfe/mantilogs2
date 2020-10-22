# Generated by Django 3.1.2 on 2020-10-22 01:56

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('leopard_gecko', '0006_auto_20201020_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='egg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='tank_object',
            name='picture',
            field=models.ImageField(blank=True, upload_to='leo_tankobj_pics/'),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('picture', models.ImageField(blank=True, upload_to='leo_gallery_pics/')),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('notes', models.TextField(blank=True, max_length=2048)),
                ('gecko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leopard_gecko.gecko')),
            ],
        ),
    ]
