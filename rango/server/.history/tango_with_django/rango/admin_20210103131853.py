from django.contrib import admin
from .models import Category, Page, User

# Register your models here.

class PageInline(admin.TabularInline):
    # list_display = ('title', 'category', 'url')
    # fields = ('title', 'url', 'category')
    model = Page
    extra = 3
    


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes')
    # prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Category Information', {"fields": ['name']}),
        ('Additional Information', {'fields': ['likes', 'views'], 'classes': ['collapse']})
    )
    inlines = [PageInline]
    list_filter = ['name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(User)