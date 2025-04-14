from django.contrib import admin
from .models import Book, Category, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'formatted_price', 'stock', 'category')
    list_filter = ('binding_type', 'publisher', 'language', 'category')
    search_fields = ('title', 'author', 'isbn')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('book__title', 'user__username')