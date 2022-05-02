"""Test file for listing models"""
from django.test import TestCase
from listing.factory_data import ListingFactory


class ListingsStrTest(TestCase):
    """
    Listing model test case
    """

    @staticmethod
    def create_listing():
        """Creates a fake listing"""
        return ListingFactory()


    def test_listing_str(self):
        """Test listing model str function"""
        listing = self.create_listing()
        self.assertEqual(f"{listing.make} {listing.model} {listing.year}", str(listing))
