from django.test import TestCase
from listing.models import Listings
from listing.factory_data import ListingFactory


class ListingsStrTest(TestCase):

    @staticmethod
    def create_listing():
        """Creates a fake listing"""
        return ListingFactory()


    def test_listing_str(self):
        listing = self.create_listing()
        self.assertEqual(f"{listing.make} {listing.model} {listing.year}", str(listing))