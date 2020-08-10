from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    CATEGORIES = (
        ("HOME", "Home"),
        ("TOYS", "Toys"),
        ("ELEC", "Electronics"),
        ("TRAN", "Transport")
    )
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="images")
    created = models.DateTimeField(auto_now_add=True, blank=True)
    description = models.CharField(max_length=500)
    owner = models.CharField(max_length=64)
    category = models.CharField(
        max_length=4,
        choices=CATEGORIES,
    )

class Auction(models.Model):
    list_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    number_bids = models.IntegerField()
    started = models.DateTimeField()
    ended = models.DateTimeField()

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)