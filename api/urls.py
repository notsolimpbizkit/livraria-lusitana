from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.get_cart_items, name='api_cart_items'),
]