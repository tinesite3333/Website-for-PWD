from django import forms
from .models import DriverProfile

class DriverProfileForm(forms.ModelForm):
    class Meta:
        model = DriverProfile
        fields = ['contact_number', 'vehicle_type', 'availability', 'travel_area']
        widgets = {
            'availability': forms.TextInput(attrs={'placeholder': 'e.g. 8AM - 5PM'}),
            'travel_area': forms.TextInput(attrs={'placeholder': 'e.g. San Juan, Taft'}),
            'plate_number': forms.TextInput(attrs={'placeholder': 'e.g. ABC-1234'}),
        }
