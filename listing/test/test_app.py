"""Test file for app configuration"""
from django.apps import apps
from django.test import TestCase
from listing.apps import ListingConfig


class ListingConfigTest(TestCase):
    """Test cases for listing app"""

    def test_apps(self):
        """Test app configuration"""
        self.assertEqual(ListingConfig.name, 'listing')
        self.assertEqual(apps.get_app_config('listing').name, 'listing')
