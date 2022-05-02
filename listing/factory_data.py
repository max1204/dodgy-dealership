"""Factory module to generate fake data for the database."""
import factory
import faker
from factory.django import DjangoModelFactory
from faker.providers.phone_number import Provider
from faker_vehicle import VehicleProvider

from listing import models as tables

MIN_PRICE = 1000
MAX_PRICE = 100000


class IndiaPhoneNumberProvider(Provider):
    """
    A Provider for phone number.
    """

    def india_phone_number(self):
        """Return an Indian phone number"""
        return f'+91 {self.msisdn()[3:]}'


fake = faker.Faker()
fake.add_provider(VehicleProvider)
fake.add_provider(IndiaPhoneNumberProvider)


class ListingFactory(DjangoModelFactory):
    """Factory class to generate fake Listings."""

    class Meta:
        model = tables.Listings

    seller_name = factory.Faker("name")
    price = factory.Faker('pyint', min_value=1000, max_value=100000)
    contact_number = fake.india_phone_number()
    year = factory.Faker('pyint', min_value=1886, max_value=2021)
    make = factory.Sequence(lambda n: fake.vehicle_make())
    model = factory.Sequence(lambda n: fake.vehicle_model())


class InterestFactory(DjangoModelFactory):
    """Factory class to generate Interests."""

    class Meta:
        model = tables.Interest

    name = factory.Faker('name')
    contact_number = fake.india_phone_number()
    listing = ListingFactory()
