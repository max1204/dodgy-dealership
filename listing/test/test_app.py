from django.apps import apps
from django.test import TestCase
from listing.apps import ListingConfig


class ListingConfigTest(TestCase):

    def test_apps(self):
        self.assertEqual(ListingConfig.name, 'listing')
        self.assertEqual(apps.get_app_config('listing').name, 'listing')