"""This module defines models for the application."""
import uuid
from datetime import datetime

from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models


def current_year():
    """Returns the current year"""
    return datetime.today().year


class Listings(models.Model):
    """Class for Listings Table in the database"""
    CONDITION_CHOICES = (
        ('poor', 'Poor'), 
        ('fair', 'Fair'), 
        ('good', 'Good'),
        ('excellent', 'Excellent')
    )

    id = models.UUIDField(
            primary_key=True, 
            default=uuid.uuid4, 
            editable=False
        )
    phone_regex = RegexValidator(
        regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$',
        message=
        "Phone number must be entered in the format: '+99 9999999'. Up to 15 digits allowed."
    )
    seller_name = models.CharField(max_length=30)
    contact_number = models.CharField(validators=[phone_regex],
                                      max_length=20,
                                      blank=False)
    make = models.CharField(max_length=20, blank=False)
    model = models.CharField(max_length=30, blank=False)
    year = models.PositiveIntegerField(
        default=current_year(),
        validators=[
            MinValueValidator(1886),
            MaxValueValidator(current_year())
        ]
    )  # Min Value if 1886 because that was the time the first car was made
    condition = models.CharField(choices=CONDITION_CHOICES,
                                 default='poor',
                                 max_length=9)
    price = models.IntegerField(
        validators=[MinValueValidator(1000),
                    MaxValueValidator(100000)])
    created_at = models.DateTimeField(auto_now_add=True)
    sold = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.make} {self.model} {self.year}"


class Interest(models.Model):
    """Class for Interest Table in database."""

    CONDITION_CHOICES = (
        ('open', 'Open'), 
        ('in_process', 'In Process'),
        ('closed', 'Close'), 
        ('cancelled', 'Cancelled')
    )
    phone_regex = RegexValidator(
        regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$',
        message=
        "Phone number must be entered in the format: '+99 9999999'. Up to 15 digits allowed."
    )
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    name = models.CharField(
        max_length=30
    )
    contact_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        choices=CONDITION_CHOICES,
        default='open',
        max_length=15
    )
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE)
