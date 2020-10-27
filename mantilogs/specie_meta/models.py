from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime

# Create your models here.
class Specie(models.Model):
    """Meta data about species, scientific name, etc."""
    # Common Name
    common_name = models.CharField(max_length=240, default="")
    # Species
    species = models.CharField(max_length=240, default="")
    # Species Synonyms (Array of CharFields)
    species_synonyms = ArrayField(
        models.CharField(max_length=240, default=""), default=list, blank=True
    )
    # Domain
    domain = models.CharField(max_length=240, default="")
    # Phylum
    phylum = models.CharField(max_length=240, default="")
    # Class
    specie_class = models.CharField(max_length=240, default="")
    # Order
    order = models.CharField(max_length=240, default="")
    # Family
    family = models.CharField(max_length=240, default="")
    # Genus
    genus = models.CharField(max_length=240, default="")
    # Discovered by
    discoverer = models.CharField(max_length=240, default="")
    # Discovered date
    discovery_date = models.DateField(default=datetime.date.today)
    # Lifespan
    lifespan = models.CharField(max_length=240, default="")
    # Interesting Facts (Array of CharFields)
    interesting_facts = ArrayField(
        models.CharField(max_length=2048, default=""), default=list, blank=True, help_text="Separated by comas"
    )
    # Natural Habitat
    natural_habitat = models.CharField(max_length=240, default="")
    # Temperature range
    temperature_range = models.CharField(max_length=240, default="")
    # Humidity range
    humidity_range = models.CharField(max_length=240, default="")
    # Diet
    diet = ArrayField(
        models.CharField(max_length=240, default=""), default=list, help_text="Coma separated list."
    )
    # Behaviour
    behaviour = models.TextField(max_length=3240, default="")
    # Temperature-dependant Sex Determination
    tsd = models.BooleanField(default=False, help_text="Temperature-dependant Sex Determination")
    # Breeding Information
    breeding_info = models.TextField(max_length=5000, default="")
    # Active breeding time
    active_breeding_time = models.CharField(max_length=240, default="", help_text="eg; June, Summer, or Summer and Fall")
    # Average offspring per breeding session
    average_yearly_offspring = models.IntegerField(default=0)
    # Habitat Requirements
    habitat_requirements = models.TextField(max_length=5000, default="")
    # Information
    other_information = models.TextField(max_length=12000, default="")
    # Picture
    picture = models.ImageField(upload_to='meta_pictures/', default='nope.jpeg')
