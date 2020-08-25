from django.contrib import admin

from .models import User, Listing, Auction, Watchlist, Comment

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = (
        "name", 
        "price", 
        "description", 
        "image",
        "category",
        "owner",
        "status",
    )
    list_editable = list_display
    list_display_links = None

class CommnetAdmin(admin.ModelAdmin):
    list_display = (
        "listing",
        "comment",
        "date",
        "author",
    )
    list_editable = list_display
    list_display_links = None

class AuctionAdmin(admin.ModelAdmin):
    list_display = (
        "listing",
        "current_bid",
        "date_placed",
        "user",
        "winner",
    )
    list_editable = list_display
    list_display_links = None
    
admin.site.register(User)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Auction, AuctionAdmin)
admin.site.register(Watchlist)
admin.site.register(Comment, CommnetAdmin)

