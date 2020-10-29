from django.db import models
import datetime
import uuid


class Item(models.Model):
    """Individual Items"""
    def __str__(self):
        return f"{self.name}"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Name
    name = models.CharField(max_length=120, default="")
    # Brand
    brand = models.CharField(max_length=120, default="")
    # Price
    price = models.FloatField(default=0.00)
    # Expires - Should track as it's own model.
    #expires = models.DateField(default=datetime.date.today)
    # Description
    description = models.TextField(max_length=1200, default="")
    # UPC
    upc = models.ImageField(upload_to='upcs/', blank=True, null=True)
    # Picture
    picture = models.ImageField(upload_to='item_pics/', blank=True, null=True)
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
    item_type = models.CharField(max_length=120, choices=item_types, default='Other')


class Order(models.Model):
    """Ordered Items"""
    def __str__(self):
        return f"{self.order_date} : [{self.items}] from {self.ordered_from} for {self.total_cost}"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    items = models.ManyToManyField(Item)
    order_id = models.CharField(max_length=120, default="")
    total_cost = models.FloatField(default=0.00)
    ordered_from = models.CharField(max_length=120, default="")
    order_date = models.DateField(default=datetime.date.today)


class Inventory(models.Model):
    """Item meta, tracks how many of each item are in inventory."""
    def __str__(self):
        return f"{self.count} x {self.item}"
    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True)
    count = models.IntegerField(default=0)


class Item_Consumption(models.Model):
    """Every time an item is used and how"""
    def __str__(self):
        return f"Consumed {self.item} on {self.date_consumed}"
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_consumed = models.DateField(default=datetime.date.today)
    expired = models.BooleanField(default=False)
    notes = models.TextField(max_length=1200, default="")


class Item_Expiration(models.Model):
    """So you know when to look through stock and throw stuff out."""
    def __str__(self):
        return f"{self.item} expires {self.expiration_date}"
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, primary_key=False)
    expiration_date = models.DateField(default=datetime.date.today)
    #num_items_expired = models.IntegerField(default=1)
