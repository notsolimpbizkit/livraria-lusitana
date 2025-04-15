from django.contrib import admin
from .models import Book, Category, Review
from livraria_project.admin import admin_site
from django.utils.safestring import mark_safe


#@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)

#@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'formatted_price', 'stock', 'category')
    list_filter = ('binding_type', 'publisher', 'language', 'category')
    search_fields = ('title', 'author', 'isbn')
    readonly_fields = ('created_at', 'updated_at')

    def book_cover(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="75" />')
        return "No cover"
    book_cover.short_description = 'Cover'

#@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('book__title', 'user__username')


admin_site.register(Category, CategoryAdmin)
admin_site.register(Book, BookAdmin)
admin_site.register(Review, ReviewAdmin)