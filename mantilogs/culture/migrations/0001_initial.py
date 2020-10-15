# Generated by Django 3.1 on 2020-10-15 16:34

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', help_text='I usually name mine after stickers I have on their tanks.', max_length=250)),
                ('creation_date', models.DateField(default=datetime.date.today)),
                ('notes', models.TextField(default='', max_length=25000)),
                ('retired', models.BooleanField(default=False, help_text='Retired usually means everything died but you could have other reasons.')),
                ('profile_picture', models.ImageField(default='nope.jpeg', upload_to='culture_prof_pics/')),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', help_text="If you don't know, make one up.", max_length=250)),
                ('ingredients', models.TextField(default='Ingredient 1, Ingredient 2', help_text='Ingredients separated by comma.', max_length=25000)),
                ('recipe', models.TextField(default='', help_text='If you have a recipe with ratios you can put it here.', max_length=250000)),
                ('notes', models.TextField(default='', max_length=25000)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('notes', models.TextField(default='', max_length=25000)),
                ('added_feed', models.BooleanField(default=False)),
                ('added_watering_media', models.BooleanField(default=False, help_text='Could just be water, makes no difference to me.')),
                ('cleaned_culture', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('common_name', models.CharField(default='', help_text='eg; Darkling Beetle', max_length=250)),
                ('scientific_name', models.CharField(default='', help_text='eg; Tenebrionidae', max_length=250)),
                ('specie_class', models.CharField(default='', help_text='eg; Insecta', max_length=250)),
                ('family', models.CharField(default='', help_text='eg; Tenebrionidae', max_length=250)),
                ('order', models.CharField(default='', help_text='eg; Beetles', max_length=250)),
                ('notes', models.TextField(default='', max_length=25000)),
            ],
        ),
        migrations.CreateModel(
            name='Quarantine',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=None)),
                ('reason', models.TextField(default='', max_length=25000)),
                ('culture', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='culture.culture')),
            ],
        ),
        migrations.AddField(
            model_name='culture',
            name='feed',
            field=models.ManyToManyField(default=None, to='culture.Feed'),
        ),
        migrations.AddField(
            model_name='culture',
            name='parent_culture',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='culture.culture'),
        ),
        migrations.AddField(
            model_name='culture',
            name='specie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='culture.specie'),
        ),
    ]
