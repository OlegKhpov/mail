# Generated by Django 3.0.8 on 2020-08-22 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0033_remove_auction_number_bids'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='winner',
            field=models.BooleanField(default=False),
        ),
    ]