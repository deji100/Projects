
from django.urls import path
from . import views

urlpatterns = [
    path('', views.current_datetime, name='current_datetime'),
    path('<int:time>/', views.hour_ahead, name='hour_ahead'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('thanks/', views.thanks, name='thanks'),
    path('add_publisher/', views.add_publisher, name='add_publisher')
]