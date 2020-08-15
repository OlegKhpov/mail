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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    created = models.DateTimeField(default=timezone.now, blank=True)
    description = models.TextField(max_length=640)
    status = models.BooleanField(default=True)
    category = models.CharField(
        max_length=4,
        choices=CATEGORIES,
    )

    def __str__(self):
        return self.name

class Auction(models.Model):
    list_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    number_bids = models.IntegerField()
    current_bid = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    started = models.DateTimeField()
    ended = models.DateTimeField()

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    watchlist = []