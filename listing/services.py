"""Service module for all the functionality that interacts with database writes"""
from .models import Listings, Interest
from .forms import InterestForm

def make_car_available(listing_id: str) -> bool:
    """
    Makes a car available again
    input : id : str
    returns: bool
    """
    try:
        listing = Listings.objects.get(id=listing_id)
        listing.sold = False
        listing.save()

        interest = Interest.objects.get(listing=listing, status='open')
        interest.status = "cancelled"
        interest.save()

        return True
    except Listings.DoesNotExist:
        return False
    except Interest.DoesNotExist:
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
