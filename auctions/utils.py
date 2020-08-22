from .models import User, Listing, Auction, Watchlist

def get_watchlist(user):
    watchlist = []
    if not user.is_authenticated:
        return watchlist
    wl = user.watchlist_set.all()
    for item in wl:
        watchlist.append(item.item_of_wl())
    return watchlist

def check_bid(bid, listing):
    if bid == '' or not bid.isnumeric():
        bid = 0
    if int(bid) <= listing.price:
        return False
    return True

def save_bid(listing, user, new_bid):
    new = listing.auction_set.create(current_bid=new_bid, user=user)
    new.save()