from django.contrib import admin
from .models import Order, OrderItem
from livraria_project.admin import admin_site

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('formatted_price', 'formatted_line_total')

#@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'status', 'formatted_total')
    list_filter = ('status', 'order_date')
    search_fields = ('user__username', 'user__email', 'shipping_address')
    inlines = [OrderItemInline]
    readonly_fields = ('order_date', 'formatted_total')

admin_site.register(Order, OrderAdmin)