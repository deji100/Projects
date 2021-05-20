from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(ShippingAddress)
admin.site.register(OrderProduct)
# admin.site.register(Complaint)
admin.site.register(SavedProduct)
admin.site.register(Comment)