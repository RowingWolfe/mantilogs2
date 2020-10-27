from django.db import models
import datetime
import uuid


class Item(models.Model):
    """Individual Items"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Name
    name = models.CharField(max_length=120, default="")
    # Brand
    brand = models.CharField(max_length=120, default="")
    # Price
    price = models.FloatField(default=0.00)
    # Expires
    expires = models.DateField(default=datetime.date.today)
    # Description
    description = models.TextField(max_length=1200, default="")
    # UPC
    upc = models.ImageField(upload_to='upcs/', blank=True, null=True)
    # Item Type (Char Choices)
    item_types = [
        ('Feed', 'Feed'),
        ('Watering Media', 'Watering Media'),
        ('Substrate', 'Substrate'),
        ('Habitat Item', 'Habitat Item'),
        ('Heat Pad/Wire', 'Heat Pad/Wire'),
        ('Habitat Tank', 'Habitat Tank'),
        ('Cleaning Product', 'Cleaning Product'),
        ('Incubator', 'Incubator'),
        ('Tool', 'Tool'),
        ('Dietary Supplement', 'Dietary Supplement'),
        ('Other', 'Other')
    ]


class Order(models.Model):
    """Ordered Items"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    items = models.ManyToManyField(Item)
    order_id = models.CharField(max_length=120, default="")
    total_cost = models.FloatField(default=0.00)
    ordered_from = models.CharField(max_length=120, default="")


class Inventory(models.Model):
    """Item meta, tracks how many of each item are in inventory."""
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)


class Item_Consumption(models.Model):
    """Every time an item is used and how"""
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_consumed = models.DateField(default=datetime.date.today)
    expired = models.BooleanField(default=False)
    notes = models.TextField(max_length=1200, default="")