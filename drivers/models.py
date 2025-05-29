from django.db import models
from django.conf import settings


class DriverProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    
    vehicle_type = models.CharField(max_length=50, choices=[
        ('Tricycle', 'Tricycle'),
        ('Motorcycle', 'Motorcycle'),
        ('Multicab', 'Multicab'),
        ('Bus', 'Bus')
    ])
    
    availability = models.CharField(max_length=100)
    travel_area = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.user.username} - {self.vehicle_type}"
