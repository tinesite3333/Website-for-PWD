# pwds/models.py
from django.conf import settings
from django.db import models

class PWDProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15, blank=True)
    disability_type = models.CharField(max_length=100, blank=True)
    travel_needs = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
