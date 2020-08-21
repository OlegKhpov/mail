from .models import User, Listing, Auction, Watchlist

def get_watchlist(user):
    watchlist = []
    wl = user.watchlist_set.all()
    for item in wl:
        watchlist.append(item.item_of_wl())
    return watchlist