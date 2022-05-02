"""Model Forms for The application"""
from django import forms
from .models import Listings, Interest


class ListingForm(forms.ModelForm):
    """Listing Model Form."""

    class Meta:
        model = Listings
        fields = ['seller_name', 'contact_number', 'make', 'model', 'year', 'condition', 'price']


class InterestForm(forms.ModelForm):
    """Interest Model form."""

    class Meta:
        model = Interest
        fields = ['name', 'contact_number']
