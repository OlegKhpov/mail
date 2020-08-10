from django.contrib import admin

from .models import User, Listing, Auction, Watchlist

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = (
        "name", 
        "price", 
        "description", 
        "image", 
        "owner", 
        "category",
    )

admin.site.register(User)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Auction)
admin.site.register(Watchlist)

