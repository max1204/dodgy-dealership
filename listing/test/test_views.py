"""Test Case for the views for listing module"""
from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase
from django.urls import reverse
from listing.factory_data import InterestFactory, ListingFactory
from listing.models import Interest, Listings


class HomeTest(TestCase):
    """Home View test case"""

    @staticmethod
    def create_listing():
        """Create a fake listing"""
        return ListingFactory()

    def test_home(self):
        """
        This Page checks the URL for the status_code
        """
        listing = self.create_listing()
        url = reverse('home')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(listing.seller_name, str(resp.content))


class LoginTest(TestCase):
    """Test class for login view"""

    def setUp(self):
        self.credentials = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'secret',
            'is_active': True
        }
        get_user_model().objects.create_user(**self.credentials)

    def test_login(self):
        """Test Login with credentials"""
        resp = self.client.login(username=self.credentials.get('email'),
                                 password=self.credentials.get('password'))
        self.assertTrue(resp)

    def test_login_fail(self):
        """Test Login with credentials Fail"""
        resp = self.client.login(username=self.credentials.get('email'),
                                 password=self.credentials.get('pssword'))
        self.assertFalse(resp)


class AddListingTest(TestCase):
    """Test case for adding a listing"""

    @staticmethod
    def create_listing():
        """Create a fake listing"""
        return ListingFactory()

    def test_create_listing_success(self):
        """Create listing test success."""
        listing = self.create_listing()
        Listings.objects.all().delete()
        data = {
            'seller_name': listing.seller_name,
            'contact_number': listing.contact_number,
            'make': listing.make,
            'year': listing.year,
            'price': listing.price,
            'sold': listing.sold,
            'model': listing.model,
            'condition': listing.condition
        }
        url = reverse('list_car')
        resp = self.client.post(url, data=data, follow=True)
        assert Listings.objects.all().count() == 1
        assert resp.status_code == 200

    def test_create_listing_failure(self):
        """Create listing fail"""
        listing = self.create_listing()
        Listings.objects.all().delete()
        data = {
            'make': listing.make,
            'year': listing.year,
            'model': listing.model,
            'condition': listing.condition
        }
        url = reverse('list_car')
        resp = self.client.post(url, data=data, follow=True)
        assert Listings.objects.all().count() == 0
        assert resp.status_code == 200


class MakeAvailableTest(TestCase):
    """Test case to make a car available again"""

    def setUp(self):
        self.credentials = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'secret',
            'is_active': True
        }
        self.listing = ListingFactory(sold=True)
        self.interest = InterestFactory(listing=self.listing)
        get_user_model().objects.create_user(**self.credentials)


    def test_make_available(self):
        """Make a car available again."""
        url = reverse('make_available', kwargs={'id': self.interest.listing.id})
        self.client.login(
            username=self.credentials.get('email'),
            password=self.credentials.get('password')
        )
        resp = self.client.get(url, follow=True)
        listing = Listings.objects.get(id=self.listing.id)
        interest = Interest.objects.get(id=self.interest.id)
        assert resp.status_code == 200
        assert listing.sold is False
        assert interest.status == "cancelled"


class EmailTest(TestCase):
    """ Test email """
    def test_send_email(self):
        """Send message."""
        mail.send_mail('Subject here', 'Here is the message.',
            'from@example.com', ['to@example.com'],
            fail_silently=False)

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Subject here')


class InterestTest(TestCase):
    """Test case for interest"""

    def setUp(self):
        self.listing = ListingFactory()

    def test_show_interest_success(self):
        """Interest test case success"""
        url = reverse('interest', kwargs={'id': self.listing.id})
        data = {"name": "Test Buyer", "contact_number": "+9112345678912"}
        resp = self.client.post(url, data=data)
        assert resp.status_code == 200
