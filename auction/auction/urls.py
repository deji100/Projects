from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bid/<int:listing_id>/', views.process_bid_and_comment, name='bid'),
    path('listing/<int:listing_id>/', views.view_listing, name='listing'),
    path('category/<str:name>/', views.view_category, name='category'),
    path('listings/', views.view_listings, name='listings'),
    path('create/', views.create_listing, name='create'),
    path('login/', views.login_view, name='login'),
    path("logout/", views.logout_view, name="logout"),
    path('register/', views.register, name='register'), 
    # path('update_listing/', views.update_listing, name='update'),
    path('add_to_watchlist/', views.add_to_watchlist, name='add_to_watchlist'),
    path('watchlist/', views.watchlist, name='watchlist')
]
