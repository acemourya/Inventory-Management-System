from django.db import models


class Desktops(models.Model):
    # Create desktop model fields

    type = models.CharField(max_length=500, blank=False)
    price = models.IntegerField()
    choices = (
        ("AVAILABLE", "Item ready to be purchased"),
        ("SOLD", "Item already purchased"),
        ("RESTOCKING", "Item restocking in few days"),
    )
    status = models.CharField(max_length=20, choices=choices, default="SOLD")
    issues = models.CharField(max_length=100, default="No Issues")


class Laptops(models.Model):
    # Create laptop model fields

    type = models.CharField(max_length=500, blank=False)
    price = models.IntegerField()
    choices = (
        ("AVAILABLE", "Item ready to be purchased"),
        ("SOLD", "Item already purchased"),
        ("RESTOCKING", "Item restocking in few days"),
    )
    status = models.CharField(max_length=20, choices=choices, default="SOLD")
    issues = models.CharField(max_length=100, default="No Issues")


class Mobiles(models.Model):
    # Create mobile model fields

    type = models.CharField(max_length=500, blank=False)
    price = models.IntegerField()
    choices = (
        ("AVAILABLE", "Item ready to be purchased"),
        ("SOLD", "Item already purchased"),
        ("RESTOCKING", "Item restocking in few days"),
    )
    status = models.CharField(max_length=20, choices=choices, default="SOLD")
    issues = models.CharField(max_length=100, default="No Issues")
