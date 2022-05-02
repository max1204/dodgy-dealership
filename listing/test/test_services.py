from django.test import TestCase
from listing.services import create_interest, make_car_available
from listing.factory_data import InterestFactory, ListingFactory
from listing.forms import InterestForm
from listing.models import Interest, Listings
import uuid


class CreateInterestTest(TestCase):

    @staticmethod
    def create_listing():
        """Creates a fake listing"""
        return ListingFactory()

    
    def test_create_interest(self):
        """Test Create Interest Functionality."""
        listing = self.create_listing()
        form_data = {
            "name": "Test Client",
            "contact_number": "+91 7016201204",
        }
        form = InterestForm(data=form_data)

        interest = create_interest(form, listing.id)
        assert interest.listing.sold == True 
        assert interest.contact_number == "+91 7016201204"


    def test_create_interest_fail(self):
        """Test Create Interest Functionality."""
        form_data = {
            "name": "Test Client",
            "contact_number": "+91 7016201204",
        }
        form = InterestForm(data=form_data)

        with self.assertRaises(Listings.DoesNotExist):
            create_interest(form, str(uuid.uuid4()))



class MakeCarAvailableTest(TestCase):

    @staticmethod
    def create_interest():
        """Create a Mock interest."""
        return InterestFactory(listing=ListingFactory())
    
    
    def test_make_car_available(self):
        """
        Make a car available.
        """
        interest = self.create_interest()
        available = make_car_available(interest.listing.id)
        self.assertEqual(available, True)

    
    def test_make_car_available_fail(self):
        """
        Make a wrong listing available
        """
        available = make_car_available(str(uuid.uuid4()))
        self.assertEqual(available, False)