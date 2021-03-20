from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Auctioneer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Bidder(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    
class Category(models.Model):
    auctioneer = models.ForeignKey(Auctioneer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
    
class Listing(models.Model):
    auctioneer = models.ForeignKey(Auctioneer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=500)
    price = models.IntegerField(default=0)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Bid(models.Model):
    bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True, blank=True)
    bid = models.IntegerField(default=0, null=True, blank=True)
    date_time = models.DateTimeField()
    
    def __str__(self):
        return str(self.bid)


class Comment(models.Model):
    bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(max_length=300, default='none', null=True, blank=True)
    date_time = models.DateTimeField()

    def __str__(self):
        return self.comment
    

class WatchList(models.Model):
    bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE, null=True, blank=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.listing)
    