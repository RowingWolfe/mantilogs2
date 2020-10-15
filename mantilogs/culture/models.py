from django.db import models
import uuid
import datetime

# The Culture Model Redesign
class Culture(models.Model):
    """Culture Model"""
    objects = None

    def __str__(self):
        return f"{self.specie}: {self.name} - Created: {self.creation_date}"
    # ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Name
    name = models.CharField(max_length=250, default="", help_text="I usually name mine after stickers I have on their tanks.")
    # Species
    specie = models.ForeignKey('Specie', default=None, on_delete=models.CASCADE)
    # Feed(s)
    feed = models.ManyToManyField('Feed', default=None)
    # Creation Date
    creation_date = models.DateField(default=datetime.date.today)
    # Parent Culture
    parent_culture = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True, blank=True)
    # Notes
    notes = models.TextField(max_length=25000, default="", blank=True)
    # Retired (Bool)
    retired = models.BooleanField(default=False,
                                  help_text="Retired usually means everything died but you could have other reasons.")
    # Profile Picture (Why not?)
    profile_picture = models.ImageField(upload_to='culture_prof_pics/', default='nope.jpeg')


class Specie(models.Model):
    """Species Model"""
    def __str__(self):
        return f"{self.common_name} ({self.scientific_name})"
    # ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Common Name
    common_name = models.CharField(max_length=250, default="", help_text="eg; Darkling Beetle")
    # Scientific Name
    scientific_name = models.CharField(max_length=250, default="", help_text="eg; Tenebrionidae")
    # Class (class is a keyword lol.
    specie_class = models.CharField(max_length=250, default="", help_text="eg; Insecta")
    # Family
    family = models.CharField(max_length=250, default="", help_text="eg; Tenebrionidae")
    # Order
    order = models.CharField(max_length=250, default="", help_text="eg; Beetles")
    # Notes
    notes = models.TextField(max_length=25000, default="", blank=True)



class Quarantine(models.Model):
    """Quarantine Model"""
    class Meta:
        get_latest_by = "start_date"
        ordering = ["start_date"]

    def __str__(self):
        if self.end_date:
            return f"{self.culture.name} Cleared: {self.end_date}"
        else:
            return f"{self.culture.name} Date: {self.start_date} for {self.reason}"

    # ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Culture
    culture = models.ForeignKey(Culture, default=None, on_delete=models.CASCADE)
    # Start Date
    start_date = models.DateField(default=datetime.date.today)
    # End Date
    end_date = models.DateField(default=None, null=True, blank=True)
    # Reason
    reason = models.TextField(max_length=25000, default="")


class Log(models.Model):
    """Culture Log Model, the day-to-day/common stuff should be here."""

    class Meta:
        get_latest_by = "date"
        ordering = ["date"]

    def __str__(self):
        return f"{self.culture.name} at {self.date} Notes: {self.notes}"

    # ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Culture
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE, default=None)
    # Date
    date = models.DateTimeField(default=datetime.datetime.now)
    # Notes
    notes = models.TextField(max_length=25000, default="", blank=True)
    # Added Feed
    added_feed = models.BooleanField(default=False)
    # Added Watering Media
    added_watering_media = models.BooleanField(default=False,
                                               help_text="Could just be water, makes no difference to me.")
    # Cleaned Culture
    cleaned_culture = models.BooleanField(default=False)


class Feed(models.Model):
    """Culture Feed Model"""
    def __str__(self):
        return f"{self.name}"
    # ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Name
    name = models.CharField(max_length=250, default="", help_text="If you don't know, make one up.")
    # Ingredients
    ingredients = models.TextField(max_length=25000, default="Ingredient 1, Ingredient 2",
                                   help_text="Ingredients separated by comma.")
    # Recipe - If there is one.
    recipe = models.TextField(max_length=250000, default="", blank=True,
                              help_text="If you have a recipe with ratios you can put it here.")
    # Notes
    notes = models.TextField(max_length=25000, default="", blank=True)


