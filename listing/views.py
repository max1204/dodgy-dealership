"""Views for Listing Module."""
from django.contrib import messages
from django.shortcuts import redirect
from django.views import View
from django.views.generic.edit import FormView
from django_filters.views import FilterView

from . import forms
from .filters import ListingFilterSet
from .models import Listings
from .services import make_car_available, create_interest

# Create your views here.


class Home(FilterView): # pylint: disable=too-many-ancestors
    """
    View for the home page for car listing
    """
    model = Listings
    paginate_by = 10
    template_name = "listing/listing.html"
    context_object_name = 'listings'
    filterset_class = ListingFilterSet
    ordering = ["-created_at"]


class ListCar(FormView):
    """
    View for listing a new car for sale
    """
    form_class = forms.ListingForm
    template_name = 'listing/add_listing.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, message="Thank you!!! Your car is listed")
        return super().form_valid(form)


class InterestView(FormView):
    """
    View for showing interest to a new car
    """
    form_class = forms.InterestForm
    template_name = 'listing/interest.html'
    success_url = '/'

    def form_valid(self, form, **kwargs):
        create_interest(form, self.kwargs.get("id"))
        return super().form_valid(form)


class MakeAvailable(View):
    """
    Make a car available again if the deal falls through
    """
    def get(self, request, *args, **kwargs):
        """GET function for making a car avaiable"""
        if self.request.user:
            availability = make_car_available(self.kwargs.get('id'))
            if availability:
                messages.success(request, message='Car is available now')
        return redirect('home')
