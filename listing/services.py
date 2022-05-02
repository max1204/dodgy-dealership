from .models import Listings, Interest
from .forms import InterestForm

def make_car_available(id: str) -> bool:
    try:
        listing = Listings.objects.get(id=id)
        listing.sold = False
        listing.save()

        interest = Interest.objects.get(listing=listing, status='open')
        interest.status = "cancelled"
        interest.save()

        return True
    except Exception as e:
        return False


def create_interest(interest_form: InterestForm, id: str) -> Interest:
    listing = Listings.objects.get(id=id)
    obj = interest_form.save(commit=False)
    obj.listing = listing
    obj.save() 
    listing.sold = True
    listing.save()
    return obj
