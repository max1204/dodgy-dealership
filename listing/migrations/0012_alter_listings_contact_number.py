# Generated by Django 4.0.1 on 2022-01-24 12:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0011_alter_listings_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='contact_number',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^(\\+\\d{1,2}\\s)?\\(?\\d{3}\\)?[\\s.-]\\d{3}[\\s.-]\\d{4}$')]),
        ),
    ]
