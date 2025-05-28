from django.contrib import admin
from livraria_project.admin import admin_site
from .models import ContactMessage

@admin.register(ContactMessage, site=admin_site)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['subject', 'is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['created_at']
    list_editable = ['is_read']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
    
    fieldsets = (
        ('Informações do Contato', {
            'fields': ('name', 'email', 'subject')
        }),
        ('Mensagem', {
            'fields': ('message',)
        }),
        ('Informações do Sistema', {
            'fields': ('user', 'created_at', 'is_read'),
            'classes': ('collapse',)
        }),
    )