from django.core.management.base import BaseCommand
from django.db import transaction
from listing import factory_data


class Command(BaseCommand):
    help = "Generate random data for the listings"

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Adding Dummy Data")
        for i in range(2000):
            factory_data.ListingFactory()
