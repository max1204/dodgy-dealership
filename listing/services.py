"""Service module for all the functionality that interacts with database writes"""
from .models import Listings, Interest
from .forms import InterestForm


def make_listing_available(listing_id: str):
    try:
        listing = Listings.objects.get(id=listing_id)
        listing.sold = False
        listing.save()
        return listing
    except Listings.DoesNotExist:
        return False

def cancel_lead(listing: Listings):
    try:
        interest = Interest.objects.get(listing=listing, status='open')
        interest.status = "cancelled"
        interest.save()
        return True
    except Interest.DoesNotExist:
        return False

def make_car_available(listing_id: str) -> bool:
    """
    Makes a car available again
    input : id : str
    returns: bool
    """
    try:
        listing = make_listing_available(listing_id)
        if listing:
            cancel_lead(listing)
            return True
    except Exception as e:
        return False

    return False


def create_interest(interest_form: InterestForm, listing_id: str) -> Interest:
    """
    Creates an interest
    input:
        interest_form: InterestForm
        id: str
    returns:
        obj: Interest
    """
    listing = Listings.objects.get(id=listing_id)
    obj = interest_form.save(commit=False)
    obj.listing = listing
    obj.save()
    listing.sold = True
    listing.save()
    return obj
