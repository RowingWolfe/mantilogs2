from django.db import models
#from django.contrib.postgres.fields import JSONField
from datetime import date, datetime
import os

# Create your models here.


class Mantis(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(
        max_length=200, primary_key=True, help_text='Should be <StickerName>_<StickerGeneration> ie:Alien_G1')
    birthday = models.DateField(
        help_text='Should be the date of hatching.', default=date.today)
    deathday = models.DateField(
        help_text='In the case of death.', default=date.today, blank=True)
    cause_of_death = models.CharField(
        default='Old age', max_length=200, help_text='Can be Mismolt, Old age or whatever caused it.')
    nickname = models.CharField(max_length=200, default=name, blank=True)
    # Logs can be found with code referencing Mantis.name
    lifestage = models.IntegerField(
        default=1, help_text="The current L# of the bug.")
    # Bool Flags
    had_fall = models.BooleanField(default=False)
    not_eatting = models.BooleanField(default=False)
    mated = models.BooleanField(default=False)
    died_unknown = models.BooleanField(
        default=False, help_text="Did the bug bite it mysteriously?")
    died_natural = models.BooleanField(
        default=False, help_text="Did they live a long and happy life?")
    generation = models.IntegerField(
        default=0, help_text="Is this the offspring of one of ours, how many generations in?")  # Gen 0 ftw.
    sticker_generation = models.IntegerField(
        default=0, help_text="How many have championed this sticker before?")  # Weeee.
    gender = models.CharField(
        max_length=12, default="Unsexed", help_text="Does the bug have wedding tackle?")
    personality = models.CharField(max_length=1200, default="I'm a standard ass bug. Can't fault me for meeting expectations.",
                                   help_text="What's the bug like? Outgoing? Skittish?")
    color = models.CharField(max_length=120, default="Uncertain",
                             help_text="Ex. Brown, Green, Half Brown Half Green, Covered in the blood of it's enemies")
    species = models.CharField(max_length=120, default="Tenodora Sinensis",
                               help_text="Species, I.E: Tenodora Sinenses, Idolomantis Diabolica, Steve")
    profile_pic_default = "/static/mantis_riding_snake1.jpg"
    profile_pic = models.CharField(max_length=260, default=profile_pic_default,
                                   help_text="Is changed every new picture, can be set manually if need be from /static/")


class Logs(models.Model):
    def __str__(self):
        return "{0}: {1} || {2}".format(self.mantis.name, self.date, self.notes)
    mantis = models.ForeignKey(Mantis, on_delete=models.CASCADE)
    date = models.DateField(
        default=date.today, help_text="What day IS it though?")
    molted = models.BooleanField(
        default=False, help_text="Has the bug molted today?")
    notes = models.CharField(max_length=1200, default="Nothing in particular",
                             help_text="Anything odd or interesting to report today?")
    fed_today = models.BooleanField(default=False)
    personality_changes = models.CharField(
        max_length=240, help_text="Any notable shifts in personality?", default="None.")
    mated = models.BooleanField(
        default=False, help_text="Have they done the horizontal monster mash today?")
    crisis_today = models.BooleanField(
        default=False, help_text="Did something stupid happen?")
    amount_fed = models.CharField(max_length=200, default="None.",
                                  help_text="How much of what did they eat? Ex: Big Piece of Mealworm, Whole housefly, 3 Neighbor kids")
    # This will eventually be something that Jake will handle, but for now...
    high_temp_last_24 = models.IntegerField(
        default=0, help_text="How high was it? Jake will do this later.")
    low_temp_last_24 = models.IntegerField(
        default=0, help_text="Also will be a Jake job later.")
    ooths_produced = models.BooleanField(
        default=False, help_text="Is this bug a mammy bug?")


# Other pictures, taken by outside cameras.
class Picture(models.Model):
    def __str__(self):
        return self.mantis.name + " @ " + str(self.date)
    mantis = models.ForeignKey(Mantis, on_delete=models.CASCADE)
    print(mantis.name)
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to='static/uploaded_pics')

# Environmental Logging.


class Environment_Log(models.Model):
    def __str__(self):
        return str(self.date) + " Environmental Log"
    # Store by date and time. Log everu X minutes?(15 maybe)
    index = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=datetime.now)
    notes = models.CharField(max_length=250, default='None')
    humidity = models.CharField(max_length=250, default='0')
    temp = models.CharField(max_length=250, default='0')
    location = models.CharField(max_length=250, default="Unspecified")


class Culture(models.Model):
    def __str__(self):
        return self.culture_name
    culture_name = models.CharField(
        max_length=50, default='Name Me', help_text="Sticker on the culture")
    aprox_population = models.CharField(
        max_length=50, default='100', help_text="Estimated numbers")
    culture_type = models.CharField(
        max_length=120, default="Mealworm", help_text="What's in it?")
    culture_bedding = models.CharField(
        max_length=120, default="Oatato", help_text="What are they in?")
    culture_watering = models.CharField(
        max_length=120, default="Beetle Jelly", help_text="What are they getting their water from?")
    culture_notes = models.CharField(
        max_length=360, default="None", help_text="Notes about the overall culture")
    culture_creation_date = models.DateField(
        default=date.today, help_text="When was this culture created?")
    culture_retired = models.BooleanField(
        default=False, help_text="Has it been retired or the feeders removed or died?")
    had_mass_dieoff = models.BooleanField(default=False, help_text="Has this culture ever suffered a mass dieoff?")
    quarantined = models.BooleanField(default=False, help_text="Is this culture quarantined from other cultures for some reason?")
    quarantine_reasons = models.CharField(max_length=400, default="None", help_text="CSV: Mites, Unknown Worms, Recent Mass Death of Unknown Cause, etc")
    parent_culture=models.CharField(max_length=120, default="None", help_text="TROGDORRRRRRRRRRR wants to know what culture begat this one.")
    culture_health=models.CharField(max_length=120, default="Good", help_text="Good, Poor, Unknown, Destroyed, Collapsed (This will be a drop-down when I write the forms.)")
    gut_loading = models.BooleanField(default=False);


class Culture_Log(models.Model):
    def __str__(self):
        return str(self.date) + " " + self.culture.culture_name
    date = models.DateField(default=date.today)
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    log_notes = models.CharField(
        max_length=1200, default='None', help_text="Anything to note.")
    changed_watering_media = models.BooleanField(default=False)
    complete_food_change = models.BooleanField(default=False, help_text="Dumped out the old food, put in fresh.")
    added_fresh_food = models.BooleanField(default=False, help_text="Added food to old food.")
    food_added = models.CharField(max_length=200, default="None", help_text="Eg; Fluker's Cricket Diet, Orange Cubes, etc")
    cleaned_culture_tank = models.BooleanField(default=False)
    mite_infestation = models.BooleanField(default=False)
    mass_death = models.BooleanField(default=False)
    quarantined = models.BooleanField(default=False)
    reason_for_quarantine = models.CharField(max_length=500, default="None", help_text="Mites, Mold, etc. I need to make this a drop down too.")
    recent_spawning_activity = models.BooleanField(default=False, help_text="Fresh eggs, ooths, evidence of them doing the horizontal monster mash?")
    high_temp_last_24 = models.IntegerField(default=0, help_text="You could use the logging endpoints or manually input the temp. Code assumes F, will change if needed.") 
    low_temp_last_24 = models.IntegerField(default=0, help_text="You could use the logging endpoints or manually input the temp. Fahrenheit. ^ ") 



class Gecko(models.Model):
    def __str__(self):
        return f"{self.name} || Morphs:{self.morphs} Birthdate: {self.birthday}"
    name = models.CharField(
        max_length=200, primary_key=True, help_text='Gecko name')
    father = models.CharField(max_length=200,default="Unknown")
    mother = models.CharField(max_length=200,default="Unknown")
    birthday = models.DateField(
        help_text='Should be the date of hatching or aprox.', default=date.today)
    deathday = models.DateField(
        help_text='In the case of death.', default=date.today, blank=True)
    cause_of_death = models.CharField(
        default='Old age', max_length=200, help_text='Can be Mismolt, Old age or whatever caused it.')
    nickname = models.CharField(max_length=200, default="None", blank=True)
    # Logs can be found with code referencing Mantis.name
    # Bool Flags
    mated = models.BooleanField(default=False)
    died_unknown = models.BooleanField(
        default=False, help_text="Did the poor sod bite it mysteriously?")
    died_natural = models.BooleanField(
        default=False, help_text="Did they live a long and happy life?")
    generation = models.IntegerField(
        default=0, help_text="Is this the offspring of one of ours, how many generations in?")  # Gen 0 ftw.
    gender = models.CharField(
        max_length=12, default="Unsexed", help_text="Does the gecko have wedding tackle?")
    personality = models.CharField(max_length=1200, default="I'm a standard ass Gecko. Can't fault me for meeting expectations.",
                                   help_text="What's the Gecko like? Outgoing? Skittish?")
    morphs = models.CharField(max_length=120, default="Unknown",
                               help_text="Blizzard, Albino_Bell, Leucistic, POSSIBLE_Melanistic")
    profile_pic_default = "/static/gecko.jpg"
    profile_pic = models.CharField(max_length=260, default=profile_pic_default,
                                   help_text="Is changed every new picture, can be set manually if need be from /static/")
    picture = models.ImageField(upload_to='gecko_images/', default='nope.jpeg')
    #HERE THERE BE DRAGONS! (Or smol nippy gexles.)


class Gecko_Log(models.Model):
    def __str__(self):
        return "{0}: {1} ||      {2}".format(self.gecko.name, self.date, self.notes)
    gecko = models.ForeignKey(Gecko, on_delete=models.CASCADE)
    date = models.DateField(
        default=date.today, help_text="What day IS it though?")
    molted = models.BooleanField(
        default=False, help_text="Has the gecko molted today?")
    notes = models.CharField(max_length=1200, default="Nothing in particular",
                             help_text="Anything odd or interesting to report today?")
    fed_today = models.BooleanField(default=False)
    personality_changes = models.CharField(
        max_length=240, help_text="Any notable shifts in personality?", default="None")
    mated = models.BooleanField(
        default=False, help_text="Have they done the horizontal monster mash today?")
    crisis_today = models.BooleanField(
        default=False, help_text="Did something stupid happen?")
    amount_fed = models.CharField(max_length=200, default="None",
                                  help_text="How much of what did they eat? Ex: Big Piece of Mealworm, Whole housefly, 3 Neighbor kids")
    # TODO: Rebuild the env logger.
    high_temp_last_24 = models.IntegerField(
        default=0, help_text="How high was it? Jake will do this later.")
    low_temp_last_24 = models.IntegerField(
        default=0, help_text="Also will be a Jake job later.")
    eggs_produced = models.BooleanField(
        default=False, help_text="Has this gecko laid eggs today?")
    number_eggs_produced = models.IntegerField(default= 0, help_text="How many eggs if any?")
    color_changes = models.CharField(max_length=200, default="None", help_text="Any notable changes in color? More orange, less orange, black feet, yellow feet, white left front foot, etc.")
    calcium_fortified = models.BooleanField(default=True, help_text="Food dusted in calcium?")
    calc_with_vit_d = models.BooleanField(default=False, help_text="Food dusted with calcium and vitamin D")
    multivitamin_fortified = models.BooleanField(default=False, help_text="Dusted with a multivit?")
    moist_hide_media_changed = models.BooleanField(default=False, help_text="Changed out stanky moss?")
    moisturized_moist_hide = models.BooleanField(default=False, help_text="Spritz the moss?")
    water_bowl_good = models.BooleanField(default=False, help_text="Enough water in the water bowl?")
    has_defecated = models.BooleanField(default=False, help_text="Did the gecko drop a deuce?")
    cleaned_water_bowl = models.BooleanField(default=False, help_text="Have to clean the water bowl?")
    cleaned_food_bowl = models.BooleanField(default=False, help_text="Have to clean the food bowl?")
    habitat_full_clean = models.BooleanField(default=False, help_text="Did the habitat get cleaned today?")

class Gecko_Morph(models.Model):
    def __str__(self):
        return f"{self.name}"
    #name
    name = models.CharField(
        max_length=200, primary_key=True, help_text='Name of Morph')
    #discover date default today because fux it.
    date = models.DateField(default=date.today, help_text="Date of discovery?")
    #visual
    visual = models.BooleanField(
        default=False, help_text="Is it a visual trait?")
    #eye morph bool
    eye = models.BooleanField(
        default=False, help_text="Is it an eye morph?")
    #size morph bool
    size = models.BooleanField(
        default=False, help_text="Is it a size trait, eg; giant, etc??")
    #primary features
    primary_features = models.CharField(max_length=1200, help_text="Primary known features of the morph. eg; Orange Skin")
    #secondary featuers
    secondary_features = models.CharField(max_length=1200, help_text="Secondary known features of the morph. eg; Red eyes if a certain type of albino.")
    #estimated transmission to offspring %
    transmission_chance_estimate = models.IntegerField(default=0, help_text="Chance of passing it off based on how many children were born with the trait as known G2+ from the DB.")
    #recessive bool Rewrute descriptions later. implement now.
    recessive = models.BooleanField(
        default=False, help_text="Is it recessive?")
    #dominant bool
    dominant = models.BooleanField(
        default=False, help_text="Is it dominant?")
    #codominant bool
    codominant = models.BooleanField(
        default=False, help_text="Is it codominant?")
    #polygenic
    polygenic = models.BooleanField(
        default=False, help_text="Is it polygenic?")
    #potential issues
    potential_issues = models.CharField(max_length=1200, default="None known.", help_text="Prone to boneitis, etc.")
    #bool for combo morph (If this morph is a combo)
    combo_morph = models.BooleanField(
        default=False, help_text="Is this morph a combination of other morphs?")
    #morphs to make this morph if combo morph default none
    #TODO: Model this as a many_to_many perhaps?
    morphs_required = models.CharField(max_length=1200, default="None", help_text="Traits required to create, eg; Tangerine, Melanistic, Raptor")


class Gecko_Egg_Clutch(models.Model):
    date_produced = models.DateTimeField(auto_now=True, auto_now_add=False)
    father = models.ForeignKey(Gecko, on_delete=models.CASCADE, related_name="gecko_father")
    mother = models.ForeignKey(Gecko, on_delete=models.CASCADE, related_name="gecko_mother")
    eggs = models.IntegerField()
    slugs = models.IntegerField()
    notes = models.CharField(max_length=255)

class Mantis_Ooth(models.Model):
    date_produced = models.DateTimeField(auto_now=True, auto_now_add=False)
    father = models.ForeignKey(Mantis, on_delete=models.CASCADE, related_name="mantis_father")
    mother = models.ForeignKey(Mantis, on_delete=models.CASCADE, related_name="mantis_mother")
    notes = models.CharField(max_length=255)


class Inventory_Item(models.Model):
    """Inventory Management for food, supplies, etc."""
    def __str__(self):
        return f"{self.stock} x {self.name} {self.size}"
    name = models.CharField(max_length=250)
    size = models.CharField(max_length=240, help_text="50oz, 10ft, 24in x 52in, etc.")
    stock = models.IntegerField(help_text="How many are in inventory?")
    links = models.JSONField(default=list)
    historical_price_data = models.JSONField(default=list)
    brand = models.CharField(max_length=255, help_text="Fluker's, ZooMed, Etc.")


class Purchase(models.Model):
    """Purchases made, total expense, store acquired from, order number. Eventually will be useful for tax reasons."""
    def __str__(self):
        return f"{self.transaction_id}: ${self.total_price} from {self.purchased_from}"
    #TODO: When writing the interfaces link up to inventory item and add items to the inventory on purchase.
    items_purchased = models.JSONField(default=list, help_text="Items in list structure.")
    purchased_from = models.CharField(max_length=200, default="Amazon", help_text="Where this purchase was made.")
    transaction_id = models.CharField(max_length=200, default="None")
    total_price = models.DecimalField(max_digits=5, decimal_places=2, help_text="Total amount paid, eg; 54.32",
                                      default=0.00)

class Inventory_Consumption(models.Model):
    """For each time an item in inventory is consumed, wether naturally or by rot or other means.
    This should allow us to track if we buy something too often, or the vendor is problematic or if we should buy
    something more often. When I do eventually write all these forms or create a secondary interface this will
    automatically reduce the count in inventory."""
    def __str__(self):
        return f"{self.item_consumed} {self.item_size}"
    item_consumed = models.ForeignKey(Inventory_Item, on_delete=models.CASCADE)
    item_size = models.CharField(max_length=200, default="6oz")
    went_bad = models.BooleanField(default=False, help_text="Did it rot, or break prematurely?")
    consumed_naturally = models.BooleanField(default=True, help_text="Did it just run out or expire as expected?")
