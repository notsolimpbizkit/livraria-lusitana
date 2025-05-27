from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('category/<int:pk>/', views.category_books, name='category_books'),
    path('search/', views.search_books, name='search_books'),
    path('review/<int:book_id>/', views.add_review, name='add_review'),
    path('get-cart-books/', views.get_cart_books, name='get_cart_books'),
    
]