from django.contrib import admin
from .models import UserProfile, Wishlist
from livraria_project.admin import admin_site

#@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'postal_code', 'phone')
    search_fields = ('user__username', 'user__email', 'city')

#@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'added_date')
    search_fields = ('user__username', 'book__title')

admin_site.register(UserProfile, UserProfileAdmin)
admin_site.register(Wishlist, WishlistAdmin)