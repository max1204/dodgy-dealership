# Generated by Django 4.0.1 on 2022-05-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0016_alter_interest_contact_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('in_process', 'In Process'), ('closed', 'Close'), ('cancelled', 'Cancelled')], default='open', max_length=15),
        ),
    ]