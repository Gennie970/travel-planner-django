from django.db import models

class TripDay(models.Model):
    date = models.CharField(max_length=20)  # "2026-04-25"

class TripItem(models.Model):
    day = models.ForeignKey(TripDay, on_delete=models.CASCADE, related_name="items")
    time = models.CharField(max_length=10)
    text = models.CharField(max_length=255)
    cost = models.IntegerField(blank=True, null=True)
