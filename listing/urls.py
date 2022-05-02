"""Module for URLs"""
from django.urls import path
from .views import Home, ListCar, InterestView, MakeAvailable

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path(
        'listcar/', 
        ListCar.as_view(), 
        name='list_car'
    ),
    path(
        'interest/<uuid:id>', 
        InterestView.as_view(), 
        name='interest'
    ),
    path(
        'make-available/<uuid:id>',
        MakeAvailable.as_view(),
        name='make_available'
    )
]
