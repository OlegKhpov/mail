from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<str:listing>", views.listing, name="listing"),
    path("create", views.create, name="create"),
    path("create_new", views.create_new, name="create_new"),
    path("close/<str:listing>", views.close_bids, name="close_bids"),
    path("my_watchlist", views.my_watchlist, name="my_watchlist"),
    path("add_to_wl/<str:listing>", views.add_to_wl, name="add_to_wl"),
    path("place_bid/<str:listing>", views.place_bid, name="place_bid"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category>", views.category, name="category"),
    path("new_comment/<str:listing>", views.new_comment, name="new_comment"),
    path("remove_from_wl/<str:listing>", views.remove_from_wl, name="remove_from_wl"),
]
