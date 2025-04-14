from django.contrib import admin
from .models import UserProfile, Wishlist

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'postal_code', 'phone')
    search_fields = ('user__username', 'user__email', 'city')

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'added_date')
    search_fields = ('user__username', 'book__title')