from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from books.models import Book, Category, Review
from orders.models import Order
from django.contrib.auth.models import User
from django.db.models import Sum, Count, Avg

@staff_member_required
def dashboard_home(request):
    # Get quick stats
    total_books = Book.objects.count()
    total_orders = Order.objects.count()
    total_users = User.objects.count()
    total_reviews = Review.objects.count()
    
    # Recent orders
    recent_orders = Order.objects.order_by('-order_date')[:5]
    
    # Low stock alert
    low_stock = Book.objects.filter(stock__lt=5).order_by('stock')[:5]
    
    # Top selling books
    top_books = Book.objects.annotate(
        times_ordered=Count('orderitem')
    ).order_by('-times_ordered')[:5]
    
    # Best rated books
    best_rated = Book.objects.annotate(
        avg_rating=Avg('reviews__rating')
    ).exclude(avg_rating__isnull=True).order_by('-avg_rating')[:5]
    
    context = {
        'total_books': total_books,
        'total_orders': total_orders,
        'total_users': total_users,
        'total_reviews': total_reviews,
        'recent_orders': recent_orders,
        'low_stock': low_stock,
        'top_books': top_books,
        'best_rated': best_rated,
    }
    
    return render(request, 'dashboard/home.html', context)