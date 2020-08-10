from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Auction(models.Model):
    CATEGORIES = {
        'TOY': 'Toys',
        'HOM': 'Home',
        'POT': 'Potions',
        'BOO': 'Books',
        'ART': 'Artifact',
    }

    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2)
    owner = models.CharField(max_length=64)
    current_bid = models.DecimalField(decimal_places=2)