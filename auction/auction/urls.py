from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('bid/<int:listing_id>/', views.process_bid_and_comment, name='bid'),
    path('listing/<int:listing_id>/', views.view_listing, name='listing'),
    path('category/<str:id>/', views.view_category, name='category'),
    path('delete/<str:pk>/', views.delete_from_watchlist, name='delete'),
    path('add_to_watchlist/<str:pk>', views.add_to_watchlist, name='add_to_watchlist'),
    path('listings/', views.view_listings, name='listings'),
    path('create/', views.create_listing, name='create'),
    path('', views.login_view, name='login'),
    path("logout/", views.logout_view, name="logout"),
    path('register/', views.register, name='register'),
    path('watchlist/', views.watchlist, name='watchlist')
]
