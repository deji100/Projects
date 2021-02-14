from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login_view"),
    path("logout/", views.logout_view, name="logout_"),
    path("register/", views.register, name="register"),
    path("create_listing/", views.create_listing, name='create_listing'),
    path("active/<int:auction_listing_id>/", views.active, name='active'),
]
