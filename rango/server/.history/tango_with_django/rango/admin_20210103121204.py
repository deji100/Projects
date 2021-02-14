from django.contrib import admin
from .models import Category, Page, User

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    fields = ('title', 'url', 'category')
    fieldsets = (
        ('', {
            "fields": ( 
                
            ),
        }),
    )
    


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes')
    # prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(User)