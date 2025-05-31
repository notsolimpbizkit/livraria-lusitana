# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('orders/', views.orders, name='orders'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/remove/<int:book_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/add/', views.add_to_wishlist, name='add_to_wishlist'),
    path('logout/', views.logout, name='logout'),
]