from django.contrib import admin
from .models import *

# Register your models here.

class AdminBid(admin.ModelAdmin):

    list_display = ('bidder', 'listing', 'bid')


admin.site.register(Auctioneer)
admin.site.register(Bidder)
admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(Comment)
admin.site.register(WatchList)
admin.site.register(Bid, AdminBid)