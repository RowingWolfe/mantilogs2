# Generated by Django 3.1 on 2020-10-27 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leopard_gecko', '0009_morph_althernate_names'),
    ]

    operations = [
        migrations.RenameField(
            model_name='morph',
            old_name='althernate_names',
            new_name='alternate_names',
        ),
        migrations.AddField(
            model_name='morph',
            name='heterozygous',
            field=models.BooleanField(default=False),
        ),
    ]
