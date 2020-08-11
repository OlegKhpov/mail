from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

class Listing(models.Model):
    CATEGORIES = (
        ("HOME", "Home"),
        ("TOYS", "Toys"),
        ("POTI", "Potions"),
        ("BOOK", "Books"),
        ("ARTI", "Artifacts"),
    )
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    created = models.DateTimeField(default=timezone.now, blank=True)
    description = models.TextField(max_length=640)
    category = models.CharField(
        max_length=4,
        choices=CATEGORIES,
    )

class Auction(models.Model):
    list_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    number_bids = models.IntegerField()
    current_bid = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    started = models.DateTimeField()
    ended = models.DateTimeField()

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    number_watchlist = models.IntegerField()