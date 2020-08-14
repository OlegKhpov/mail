from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import User, Listing, Auction, Watchlist

class new_listing_form(forms.Form):
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={
        'placeholder': 'Name',
        'rows': '1',
    }))
    image = forms.ImageField(label="Image")
    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={
        'placeholder': 'Description',
        'rows': '30',
    }))
    price = forms.DecimalField(label='Price', widget=forms.TextInput(attrs={
        'placeholder': 'Price'
        'rows': '1'
    }))

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
    if request.method == "POST":
        form = new_listing_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Name']
            description = form.cleaned_data['Description']
            price = form.cleaned_data['Price']
            image = form.cleaned_data['Image']
    return render(request, "auctions/create.html")

