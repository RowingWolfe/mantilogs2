from django.db import models
import datetime


# Create your models here.
class Gecko(models.Model):
    """Individual Gecko Model, Information about a specific gecko."""
    # ID
    # Name
    # Nickname
    # Egg
    # Birthday
    # Morphs Many To Many Morphs.
    # Gender
    # Personality
    # Profile Picture
    # Bio
    # Caretaker Notes
    # Caretaker/Owner (User FK)
    pass


class Morph(models.Model):
    """Information about gecko morphs."""
    # ID
    # Morph Name
    # Morph Type (Color, Pattern, Eye, Size) Multi-Choice
    # Color (If Applicable)
    # Discovery Date (If known)
    # Picture
    # Description
    # Is_Dangerous - bool
    # Polygenic
    # Dominant
    # Codominant
    # Incomplete_Dominant
    pass


class Log(models.Model):
    """Usually Daily. Should be simple and quick to fill out."""
    # ID
    # Time of log
    # Gecko (FK)
    # Problems
    # Notes
    # Noteworthy Personality Changes
    pass


class Feeding_Log(models.Model):
    """Log feeding"""
    # ID
    # Time
    # Gecko(FK)
    # Log(FK)
    # Feed Type (Drop Down?)
    # Feed Amount
    # Notes
    pass


class Molt(models.Model):
    """Log each molt"""
    # ID
    # Time of Molt
    # Gecko
    # Log (FK)
    # Notes
    # Problems
    # Picture (After)
    pass


class Breeding_Log(models.Model):
    """Logs each attempt at breeding."""
    # ID
    # Date
    # Mother
    # Father
    # Clutch (FK) Empty = True
    # Notes
    # Success Bool
    pass


class Clutch(models.Model):
    """Logs a collection of eggs created from a successful breeding."""
    # ID
    # Time
    # Mother
    # Father
    # Eggs
    pass


class Egg(models.Model):
    """Logs each egg from a clutch."""
    # ID
    # Clutch (FK)
    # Weight
    # Appears_healthy
    # Size (CM)
    # Name
    pass


class Tank(models.Model):
    """A tank and it's contents as well as the Gecko within."""
    # ID
    # Creation Date
    # Gecko
    # Contents Many to Many Tank Objects
    pass


class Tank_Object(models.Model):
    """Individual Objects inside a tank, water bowl, hide, etc..."""
    # ID
    # Tank (FK)
    # Date Added (Default today)
    # Name
    # Purpose
    # Notes
    # Picture (Empty-able)
    pass


class Cleaning_Log(models.Model):
    """Log of each tank cleaning/object cleaning"""
    # ID
    # Tank
    # Date
    # Full Clean
    # Cleaner Used
    # Cleaned Specific Item(s) ManyToMany Tank Objects
    pass


class Death(models.Model):
    """Logs an unfortunate occasion... but important to log nonetheless."""
    # ID
    # Gecko
    # Date
    # Reason (If Known)
    pass

