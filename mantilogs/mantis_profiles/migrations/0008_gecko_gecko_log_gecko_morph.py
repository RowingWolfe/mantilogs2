# Generated by Django 2.2.5 on 2020-07-03 20:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mantis_profiles', '0007_feeder_culture_feeder_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gecko',
            fields=[
                ('name', models.CharField(help_text='Gecko name', max_length=200, primary_key=True, serialize=False)),
                ('birthday', models.DateField(default=datetime.date.today, help_text='Should be the date of hatching or aprox.')),
                ('deathday', models.DateField(blank=True, default=datetime.date.today, help_text='In the case of death.')),
                ('cause_of_death', models.CharField(default='Old age', help_text='Can be Mismolt, Old age or whatever caused it.', max_length=200)),
                ('nickname', models.CharField(blank=True, default=models.CharField(help_text='Gecko name', max_length=200, primary_key=True, serialize=False), max_length=200)),
                ('mated', models.BooleanField(default=False)),
                ('died_unknown', models.BooleanField(default=False, help_text='Did the poor sod bite it mysteriously?')),
                ('died_natural', models.BooleanField(default=False, help_text='Did they live a long and happy life?')),
                ('generation', models.IntegerField(default=0, help_text='Is this the offspring of one of ours, how many generations in?')),
                ('gender', models.CharField(default='Unsexed', help_text='Does the gecko have wedding tackle?', max_length=12)),
                ('personality', models.CharField(default="I'm a standard ass Gecko. Can't fault me for meeting expectations.", help_text="What's the Gecko like? Outgoing? Skittish?", max_length=1200)),
                ('morphs', models.CharField(default='Unknown', help_text='Blizzard, Albino_Bell, Leucistic, POSSIBLE_Melanistic', max_length=120)),
                ('profile_pic', models.CharField(default='/static/gecko.jpg', help_text='Is changed every new picture, can be set manually if need be from /static/', max_length=260)),
            ],
        ),
        migrations.CreateModel(
            name='Gecko_Morph',
            fields=[
                ('name', models.CharField(help_text='Name of Morph', max_length=200, primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today, help_text='Date of discovery?')),
                ('visual', models.BooleanField(default=False, help_text='Is it a visual trait?')),
                ('eye', models.BooleanField(default=False, help_text='Is it an eye morph?')),
                ('size', models.BooleanField(default=False, help_text='Is it a size trait, eg; giant, etc??')),
                ('primary_features', models.CharField(help_text='Primary known features of the morph. eg; Orange Skin', max_length=1200)),
                ('secondary_features', models.CharField(help_text='Secondary known features of the morph. eg; Red eyes if a certain type of albino.', max_length=1200)),
                ('transmission_chance_estimate', models.IntegerField(default=0, help_text='Chance of passing it off based on how many children were born with the trait as known G2+ from the DB.')),
                ('recessive', models.BooleanField(default=False, help_text='Is it recessive?')),
                ('dominant', models.BooleanField(default=False, help_text='Is it dominant?')),
                ('codominant', models.BooleanField(default=False, help_text='Is it codominant?')),
                ('polygenic', models.BooleanField(default=False, help_text='Is it polygenic?')),
                ('potential_issies', models.CharField(default='None known.', help_text='Prone to boneitis, etc.', max_length=1200)),
                ('combo_morph', models.BooleanField(default=False, help_text='Is this morph a combination of other morphs?')),
                ('morphs_required', models.CharField(default='None', help_text='Traits required to create, eg; Tangerine, Melanistic, Raptor', max_length=1200)),
            ],
        ),
        migrations.CreateModel(
            name='Gecko_Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, help_text='What day IS it though?')),
                ('molted', models.BooleanField(default=False, help_text='Has the gecko molted today?')),
                ('notes', models.CharField(default='Nothing in particular', help_text='Anything odd or interesting to report today?', max_length=1200)),
                ('fed_today', models.BooleanField(default=False)),
                ('personality_changes', models.CharField(default='None', help_text='Any notable shifts in personality?', max_length=240)),
                ('mated', models.BooleanField(default=False, help_text='Have they done the horizontal monster mash today?')),
                ('crisis_today', models.BooleanField(default=False, help_text='Did something stupid happen?')),
                ('amount_fed', models.CharField(default='None', help_text='How much of what did they eat? Ex: Big Piece of Mealworm, Whole housefly, 3 Neighbor kids', max_length=200)),
                ('high_temp_last_24', models.IntegerField(default=0, help_text='How high was it? Jake will do this later.')),
                ('low_temp_last_24', models.IntegerField(default=0, help_text='Also will be a Jake job later.')),
                ('eggs_produced', models.BooleanField(default=False, help_text='Has this gecko laid eggs today?')),
                ('number_eggs_produced', models.IntegerField(default=0, help_text='How many eggs if any?')),
                ('color_changes', models.CharField(default='None', help_text='Any notable changes in color? More orange, less orange, black feet, yellow feet, white left front foot, etc.', max_length=200)),
                ('calcium_fortified', models.BooleanField(default=True, help_text='Food dusted in calcium?')),
                ('calc_with_vit_d', models.BooleanField(default=False, help_text='Food dusted with calcium and vitamin D')),
                ('multivitamin_fortified', models.BooleanField(default=False, help_text='Dusted with a multivit?')),
                ('gecko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantis_profiles.Gecko')),
            ],
        ),
    ]
