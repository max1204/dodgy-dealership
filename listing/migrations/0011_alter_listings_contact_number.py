# Generated by Django 4.0.1 on 2022-01-24 12:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0010_delete_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='contact_number',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
