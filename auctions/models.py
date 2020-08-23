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
    price = models.IntegerField()
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
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    current_bid = models.IntegerField(null=True, blank=True)
    date_placed = models.DateTimeField(default=timezone.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    winner = models.BooleanField(default=False)

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def item_of_wl(self):
        return self.item

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment = models.TextField(max_length=640)
    date = models.DateTimeField(default=timezone.now, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.listing