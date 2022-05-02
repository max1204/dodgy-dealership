"""Test class for services"""
import uuid
from django.test import TestCase
from listing.services import cancel_lead, create_interest, make_car_available
from listing.factory_data import InterestFactory, ListingFactory
from listing.forms import InterestForm
from listing.models import Listings


class CreateInterestTest(TestCase):
    """Test class for create interest functionality"""

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
        assert interest.listing.sold is True
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
    """Test make car available functionality."""

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


class CancelInterestTest(TestCase):
    """Test cancel lead functionality."""

    @staticmethod
    def create_interest():
        """Create a Mock interest."""
        return InterestFactory(listing=ListingFactory())


    def test_cancel_lead(self):
        """
        Make a car available.
        """
        interest = self.create_interest()
        available = cancel_lead(interest.listing)
        self.assertEqual(available, True)


    def test_cancel_lead_fail(self):
        """
        Make a wrong listing available
        """
        available = cancel_lead(str(uuid.uuid4()))
        self.assertEqual(available, False)