from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    def __str__(self):
        return f'{self.username}'
    

class Auction_Listing(models.Model):
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=500)
    bid = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'
    

class Bid(models.Model):
    auction_listing = models.ForeignKey(Auction_Listing, on_delete=models.CASCADE, related_name='bids')
    user = models.ManyToManyField(User)
    bid = models.IntegerField()

    def __str__(self):
        return f'{self.bid}'
    

class Comment(models.Model):
    auction = models.ForeignKey(Auction_Listing, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(max_length=200, default='Add your comment here.')

    def __str__(self):
        return f'{self.comment}'
    