# Generated by Django 3.1 on 2020-10-08 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantis_profiles', '0015_inventory_consumption_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='gecko',
            name='picture',
            field=models.ImageField(default='nope.jpeg', upload_to='gecko_images/'),
        ),
    ]