from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Auction_Listing, Comment, Bid

# Register your models here.


admin.site.register(User, UserAdmin)
admin.site.register(Auction_Listing)
admin.site.register(Comment)
admin.site.register(Bid)

