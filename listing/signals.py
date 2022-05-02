"""Module for signals for listing app"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import Interest


@receiver(post_save, sender=Interest)
def send_interest_eamil(sender, instance, created, **kwargs):
    """
    After an interest is created we need to send an email to Iron Mike
    """
    if created:
        listing = instance.listing
        commision = "{:.2f}".format(listing.price*0.05)
        message = f"""
        There is a new Lead on the platform.\n
        Vehicle Details:\n
            Make: {listing.make}\n
            Model: {listing.model}\n
            Year: {listing.year}\n
            Condition: {listing.condition}\n
        Seller Details:\n
            Seller Name: {listing.seller_name}\n
            Contact Number: {listing.contact_number}\n
        Buyer Details:\n
            Buyner Name: {instance.name}\n
            Contact Number: {instance.contact_number}\n
        Commission: {commision}
        Transferrable Amount to seller: {listing.price-listing.price*0.05}
        """
        send_mail(
            'New Lead',
            message,
            'from@example.com',
            ['mike@example.com'],
            fail_silently=False,
        )
