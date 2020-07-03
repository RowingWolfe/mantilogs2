# Generated by Django 2.2.5 on 2020-07-03 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantis_profiles', '0009_auto_20200703_1529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gecko_morph',
            old_name='potential_issies',
            new_name='potential_issues',
        ),
        migrations.AddField(
            model_name='gecko',
            name='father',
            field=models.CharField(default='Unknown', max_length=200),
        ),
        migrations.AddField(
            model_name='gecko',
            name='mother',
            field=models.CharField(default='Unknown', max_length=200),
        ),
    ]
