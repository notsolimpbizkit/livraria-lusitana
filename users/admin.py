# users/admin.py
from django.contrib import admin
from .models import UserProfile, Wishlist
from livraria_project.admin import admin_site

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_email', 'get_full_name', 'city', 'postal_code', 'phone', 'get_date_joined')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name', 'city')
    list_filter = ('city', 'preferred_language', 'user__date_joined')
    readonly_fields = ('get_email', 'get_full_name', 'get_date_joined')
    
    def get_email(self, obj):
        return obj.user.email if obj.user.email else 'Não fornecido'
    get_email.short_description = 'Email'
    get_email.admin_order_field = 'user__email'
    
    def get_full_name(self, obj):
        full_name = obj.user.get_full_name()
        return full_name if full_name else 'Não definido'
    get_full_name.short_description = 'Nome Completo'
    get_full_name.admin_order_field = 'user__first_name'
    
    def get_date_joined(self, obj):
        return obj.user.date_joined.strftime('%d/%m/%Y')
    get_date_joined.short_description = 'Data de Registro'
    get_date_joined.admin_order_field = 'user__date_joined'

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_user_email', 'book', 'added_date')
    search_fields = ('user__username', 'user__email', 'book__title')
    list_filter = ('added_date',)
    
    def get_user_email(self, obj):
        return obj.user.email if obj.user.email else 'Não fornecido'
    get_user_email.short_description = 'Email do Usuário'
    get_user_email.admin_order_field = 'user__email'

admin_site.register(UserProfile, UserProfileAdmin)
admin_site.register(Wishlist, WishlistAdmin)