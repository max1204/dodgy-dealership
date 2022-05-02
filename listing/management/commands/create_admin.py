from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Create a User for Iron Mike"

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Creating an account for Iron Mike")
        models = [User]
        for m in models:
            m.objects.all().delete()

        user = User.objects.create_user('iron_make', 'mike@example.com', 'mikeymike123')
        user.is_superuser = True
        user.save()
        
