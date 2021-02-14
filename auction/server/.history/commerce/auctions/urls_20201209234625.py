from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.loginView, name="loginView"),
    path("logout/", views.logout_view, name="logout_view"),
    path("register/", views.register, name="register"),
    path("create_listing/", views.create_listing, name='create_listing'),
    path("active/<str:auction_listing>/", views.active, name='active'),
]
