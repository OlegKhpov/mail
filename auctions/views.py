from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import User, Listing, Auction, Watchlist

def index(request):
    return render(request, "auctions/index.html",{
        "listings": Listing.objects.all()
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def listing(request, listing):
    return render(request, "auctions/listing.html", {
        "listing": Listing.objects.get(name=listing)
    })

def add_to_wl(request, listing):
    pass

def create(request):
    return render(request, "auctions/create.html", {
        "CATEGORY": Listing.CATEGORIES
    })

def create_new(request):
    if request.method == "POST":
        current_user = request.user
        name = request.POST.get("name")
        description = request.POST.get("desc")
        price = request.POST.get("stprice")
        category = request.POST.get("category_set")
        new_listing = Listing(name=name, description=description, price=price, owner=current_user, category=category)
        new_listing.save()
        return HttpResponseRedirect(reverse("index"))

def close_bids(request, listing):
    object_to_change = Listing.objects.get(name=listing)
    object_to_change.status = False
    object_to_change.save()
    return HttpResponseRedirect(reverse("index"))