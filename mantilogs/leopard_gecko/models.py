from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
import datetime
import uuid


# Create your models here.
class Gecko(models.Model):
    """Individual Gecko Model, Information about a specific gecko."""
    def __str__(self):
        if self.nickname:
            return f"{self.nickname}"
        return f"{self.name}"
    # ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Name
    name = models.CharField(max_length=120, default="Anonygex")
    # Nickname
    nickname = models.CharField(max_length=120, blank=True, default="")
    # Egg
    egg = models.ForeignKey('Egg', blank=True, null=True, on_delete=models.CASCADE)
    # Birthday
    birth_date = models.DateField(default=datetime.date.today)
    # Morphs Many To Many Morphs.
    morphs = models.ManyToManyField('Morph', blank=True, null=True)
    # Gender
    genders = [('M', 'Male'), ('F', 'Female'), ('U', 'Unsexed')]
    gender = models.CharField(max_length=60, choices=genders, default='U')
    # Personality
    personality = models.CharField(max_length=240, blank=True)
    # Profile Picture
    profile_picture = models.ImageField(upload_to='leo_prof_pics/', default='nope.jpeg')
    # Bio
    bio = models.TextField(max_length=8096, blank=True)
    # Caretaker Notes
    caretaker_notes = models.TextField(max_length=8096, blank=True)
    # Caretaker/Owner (User FK)
    caretaker = models.ForeignKey(User, on_delete=models.CASCADE)
    pass


class Morph(models.Model):
    """Information about gecko morphs."""
    def __str__(self):
        return self.morph_name
    # ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Morph Name
    morph_name = models.CharField(max_length=120)
    alternate_names = ArrayField(
        models.CharField(max_length=120, blank=True, default=""), blank=True, null=True
    )
    # Morph Type (Color, Pattern, Eye, Size) Multi-Choice
    morph_types = [('COLOR', 'Color'), ('PATTERN', 'Pattern'), ('EYE', 'Eye'), ('SIZE', 'Size'), ("NONE", 'None')]
    morph_type = models.CharField(max_length=16, choices=morph_types, default='COLOR')
    secondary_morph_type = models.CharField(max_length=16, choices=morph_types, default='NONE')
    tertiary_morph_type = models.CharField(max_length=16, choices=morph_types, default='NONE')
    # Color (If Applicable)
    color = models.CharField(max_length=120, blank=True)
    # Discovery Date (If known)
    discovery_date = models.DateField(blank=True, null=True)
    # Picture
    picture = models.ImageField(upload_to='leo_morph_pics/', default='nope.jpeg')
    # Description
    description = models.TextField(max_length=1024, blank=True)
    # Is_Dangerous - bool
    is_dangerous = models.BooleanField(default=False)
    # Polygenic
    polygenic = models.BooleanField(default=False)
    # Dominant
    dominant = models.BooleanField(default=False)
    # Codominant
    codominant = models.BooleanField(default=False)
    # Incomplete_Dominant
    incomplete_dominant = models.BooleanField(default=False)
    # Het
    heterozygous = models.BooleanField(default=False)


class Morph_Combo(models.Model):
    """Combinations of morphs that make up other morphs"""
    #ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #Morph (FK)
    morph = models.ForeignKey(Morph, on_delete=models.CASCADE, related_name='morph')
    #Required 1
    first_req_morph = models.ForeignKey(Morph, on_delete=models.CASCADE, related_name='firstreqmorph')
    #Required 2
    second_req_morph = models.ForeignKey(Morph, on_delete=models.CASCADE, related_name='secondreqmorph')
    #Required 3
    third_req_morph = models.ForeignKey(Morph, on_delete=models.CASCADE, related_name='thirdreqmorph', blank=True, null=True)
    #Required 4
    fourth_req_morph = models.ForeignKey(Morph, on_delete=models.CASCADE, related_name='fourthreqmorph', blank=True, null=True)
    #Required 5
    fifth_req_morph = models.ForeignKey(Morph, on_delete=models.CASCADE, related_name='fifthreqmorph', blank=True, null=True)
    #Required 6
    sixth_req_morph = models.ForeignKey(Morph, on_delete=models.CASCADE, related_name='sixthreqmorph', blank=True, null=True)
    #Required 7
    seventh_req_morph = models.ForeignKey(Morph, on_delete=models.CASCADE, related_name='seventhreqmorph', blank=True, null=True)
    #Required 8
    eighth_req_morph = models.ForeignKey(Morph, on_delete=models.CASCADE, related_name='eighthreqmorph', blank=True, null=True)
    #Required 9
    ninth_req_morph = models.ForeignKey(Morph, on_delete=models.CASCADE, related_name='ninthreqmorph', blank=True, null=True)
    #Required 10
    tenth_req_morph = models.ForeignKey(Morph, on_delete=models.CASCADE, related_name='tenthreqmorph', blank=True, null=True)


class Log(models.Model):
    """Usually Daily. Should be simple and quick to fill out."""
    def __str__(self):
        return f"{self.gecko} @ {self.time}"
    # ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Time of log
    time = models.DateTimeField(default=datetime.datetime.now)
    # Gecko (FK)
    gecko = models.ForeignKey('Gecko', on_delete=models.CASCADE)
    # Defecation
    defecation = models.BooleanField(default=False)
    # Behavior/Interaction
    behavior = models.TextField(max_length=2048, blank=True)
    # Problems
    problems = models.TextField(max_length=2048, blank=True)
    # Notes
    other_notes = models.TextField(max_length=2048, blank=True)
    pass


class Feeding_Log(models.Model):
    """Log feeding"""
    def __str__(self):
        return f"{self.gecko} ate {self.feed} @ {self.time}"
    # ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Time
    time = models.DateTimeField(default=datetime.datetime.now)
    # Gecko(FK)
    gecko = models.ForeignKey('Gecko', on_delete=models.CASCADE)
    # Log(FK) SHOULD BE HIDDEN, PASSED BY VIEW!
    log = models.ForeignKey('Log', on_delete=models.CASCADE)
    # Feed Type ARRAY, TODO: Make sure this works right!
    feed = ArrayField(
        models.CharField(max_length=80)
    )
    # Feed Amount -- Might not need.
    # Feed Supplement (Dropdown: Calcium, Multivitamin, Vitamin D + Calcium)
    supplements = [('CALC', 'Calcium'), ('VITD', 'Vitamin D & Calcium'), ('MULT', 'Multivitamin')]
    feed_supplement = models.CharField(max_length=40, choices=supplements, default='CALC')
    # Notes
    notes = models.TextField(max_length=2048, blank=True)
    pass


class Molt(models.Model):
    """Log each molt"""
    def __str__(self):
        return f"{self.gecko} @{self.time}"
    # ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Time of Molt
    time = models.DateTimeField(default=datetime.datetime.now)
    # Gecko
    gecko = models.ForeignKey('Gecko', on_delete=models.CASCADE)
    # Log (FK)
    log = models.ForeignKey('Log', on_delete=models.CASCADE)
    # Picture (After)
    after_molt_picture = models.ImageField(upload_to='leo_molt_pics/', blank=True)
    # Problems
    problems_with_molt = models.BooleanField(default=False)
    # Notes
    notes = models.TextField(max_length=2048, blank=True)


class Breeding_Log(models.Model):
    """Logs each attempt at breeding."""
    def __str__(self):
        return f"{self.mother} did the horizontal monster mash with {self.father} @ {self.time}"
    # ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Date
    time = models.DateTimeField(default=datetime.datetime.now)
    # Mother
    mother = models.ForeignKey('Gecko', blank=True, related_name='mother', on_delete=models.CASCADE)
    # Father
    father = models.ForeignKey('Gecko', blank=True, related_name='father', on_delete=models.CASCADE)
    # Success Bool
    successful = models.BooleanField(default=False)
    # Notes
    notes = models.TextField(max_length=2048)


class Clutch(models.Model):
    """Logs a collection of eggs created from a successful breeding."""
    def __str__(self):
        return f"{self.breeding_log.mother} & {self.breeding_log.father} @ {self.breeding_log.time}"
    # ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Time
    time = models.DateTimeField(default=datetime.datetime.now)
    # Breeding Log
    breeding_log = models.ForeignKey('Breeding_Log', on_delete=models.CASCADE)


class Egg(models.Model):
    """Logs each egg from a clutch."""
    def __str__(self):
        return f"{self.name} from {self.clutch}"
    # ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time = models.DateTimeField(default=datetime.datetime.now)
    # Clutch (FK)
    clutch = models.ForeignKey('Clutch', on_delete=models.CASCADE)
    # Weight (g)
    weight = models.FloatField(help_text="grams")
    # Size (CM)
    size = models.FloatField(help_text="cm")
    # Name
    name = models.CharField(max_length=120)
    # Appears_healthy
    appears_healthy = models.BooleanField(default=False)


class Tank(models.Model):
    """A tank and it's contents as well as the Gecko within."""
    def __str__(self):
        return f"{self.gecko}'s tank"
    # ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Creation Date
    creation_date = models.DateField(default=datetime.date.today)
    # Gecko
    gecko = models.ForeignKey('Gecko', on_delete=models.CASCADE)
    # Contents Many to Many Tank Objects
    contents = models.ManyToManyField("Tank_Object")



class Tank_Object(models.Model):
    """Individual Objects inside a tank, water bowl, hide, etc..."""
    def __str__(self):
        return f"{self.name} obtained {self.date_added}"
    # ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Date Added (Default today)
    date_added = models.DateField(default=datetime.date.today)
    # Name
    name = models.CharField(max_length=240)
    # Purpose
    purpose = models.CharField(max_length=240)
    # Retired
    retired = models.BooleanField(default=False)
    # Picture (blank-able)
    picture = models.ImageField(upload_to='leo_tankobj_pics/', blank=True)
    # Notes
    notes = models.TextField(max_length=240, blank=True)



class Tank_Cleaning_Log(models.Model):
    """Log of each tank cleaning/object cleaning"""
    def __str__(self):
        return f"{self.tank} @{self.date}"
    # ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Tank
    tank = models.ForeignKey('Tank', on_delete=models.CASCADE)
    # Date
    date = models.DateTimeField(default=datetime.datetime.now)
    # Full Clean
    full_tank_clean = models.BooleanField(default=False)
    # Cleaner Used
    cleaner_used = models.CharField(max_length=120)
    # Cleaned Specific Item(s) Array of Tank Objects (Where objects in Tank).
    items_cleaned = models.CharField(max_length=1024, blank=True)


class Death(models.Model):
    """Logs an unfortunate occasion... but important to log nonetheless."""
    def __str__(self):
        return f"{self.gecko} left us {self.time}, we'll certainly miss you."
    # ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Gecko
    gecko = models.ForeignKey('Gecko', on_delete=models.CASCADE)
    # Date
    time = models.DateTimeField(default=datetime.datetime.now)
    # Reason (If Known)
    reason = models.TextField(max_length=2048, blank=True)


class Temperatures(models.Model):
    """Stores temperatures reported from temp probes in tanks"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tank = models.ForeignKey('Tank', on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    high = models.FloatField()
    low = models.FloatField()


class Picture(models.Model):
    """For picture gallery"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=120)
    gecko = models.ForeignKey('Gecko', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='leo_gallery_pics/', blank=True)
    time = models.DateTimeField(default=datetime.datetime.now)
    notes = models.TextField(max_length=2048, blank=True)