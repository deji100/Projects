from django.contrib import admin
from .models import Category, Page, User

# Register your models here.

class PageInline(admin.stacked):
    list_display = ('title', 'category', 'url')
    # fields = ('title', 'url', 'category')
    fieldsets = (
        ('Page Information', {"fields": ('title', 'url')}),
        ('Additional Information', {'fields': ['category']})
    )
    


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes')
    # prepopulated_fields = {'slug': ('name',)}
    inlines = [PageInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(User)