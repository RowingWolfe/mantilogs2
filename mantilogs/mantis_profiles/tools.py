# Views and Models are getting too crowded,
# Herein lie the helper methods what for retrieving and formatting data.
# Among other things, probably.

from .models import Gecko_Log, Gecko

# Originally I was going to write these all as one single func but that would run slow so here we are.
# TODO: Read the docs for the ORM top to bottom and find a faster way. What I know of SQL tells me this could be
# improved.


def get_last_tank_clean(gecko):
    """Return the last time the tank was full cleaned for <gecko>"""
    if Gecko_Log.objects.filter(gecko=gecko.name).filter(habitat_full_clean=True):
        return Gecko_Log.objects.filter(gecko=gecko.name).order_by('date').filter(habitat_full_clean=True).latest('date').date


def get_last_vitd(gecko):
    """Return the last time <gecko> was given Vitamin D supplement."""
    if Gecko_Log.objects.filter(gecko=gecko.name).filter(calc_with_vit_d=True):
        return Gecko_Log.objects.filter(gecko=gecko.name).order_by('date').filter(calc_with_vit_d=True).latest('date').date


def get_last_multivit(gecko):
    """Return the last time <gecko> was given a Multivitamin Supplement."""
    if Gecko_Log.objects.filter(gecko=gecko.name).filter(multivitamin_fortified=True):
        return Gecko_Log.objects.filter(gecko=gecko.name).order_by('date').filter(multivitamin_fortified=True)\
            .latest('date').date


def get_last_defecation(gecko):
    """Return the last defecation date of <gecko>"""
    if Gecko_Log.objects.filter(gecko=gecko.name).filter(has_defecated=True):
        return Gecko_Log.objects.filter(gecko=gecko.name).order_by('date').filter(has_defecated=True).latest('date').date

def get_last_fed(gecko):
    if Gecko_Log.objects.filter(gecko=gecko.name).filter(fed_today=True):
        return Gecko_Log.objects.filter(gecko=gecko.name).order_by('date').filter(fed_today=True).latest(
            'date').date