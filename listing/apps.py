"""This file is created to help the user include any application configuration
for the app. Using this, you can configure some of the attributes of the
application."""
from django.apps import AppConfig


class ListingConfig(AppConfig):
    """Listing Config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'listing'

    def ready(self):
        import listing.signals
