"""Module for test Django form and models"""
from django.test import TestCase
from listing.factory_data import InterestFactory, ListingFactory
from listing.forms import InterestForm, ListingForm


class ListingTestCase(TestCase):
    """Test class for testing the Listing Model and form"""

    @staticmethod
    def create_listing():
        """Creates a fake listing"""
        return ListingFactory()

    def test_create_listing(self):
        """Test Create Listing"""
        listing = self.create_listing()
        assert listing.model is not None
        assert listing.price >= 1000

    def test_valid_form(self):
        """Test Listing form"""
        listing = self.create_listing()
        form_data = {
            'seller_name': listing.seller_name,
            'contact_number': listing.contact_number,
            'make': listing.make,
            'year': listing.year,
            'price': listing.price,
            'sold': listing.sold,
            'model': listing.model,
            'condition': listing.condition
        }
        form = ListingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test invlid form"""
        listing = self.create_listing()
        form_data = {
            'seller_name': listing.seller_name,
            'make': listing.make,
            'year': listing.year,
            'price': listing.price,
            'sold': listing.sold,
            'model': listing.model,
            'condition': listing.condition
        }
        form = ListingForm(data=form_data)
        self.assertFalse(form.is_valid())


class InterestTest(TestCase):
    """Interest model, form test"""

    @staticmethod
    def create_interest():
        """Create Interest"""
        return InterestFactory(listing=ListingFactory())

    def test_interest_create(self):
        """Test Create Interest"""
        i = self.create_interest()
        assert i.status == 'open'
        assert i.name is not None

    def test_interest_valid_form(self):
        """Test Valid Interest form"""
        i = self.create_interest()
        form_data = {
            'name': i.name,
            'contact_number': i.contact_number,
            'listing': i.listing
        }
        form = InterestForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_interest_invalid_form(self):
        """Test InValid Interest form"""
        i = self.create_interest()
        form_data = {'name': i.name, 'listing': i.listing}
        form = InterestForm(data=form_data)
        self.assertFalse(form.is_valid())
