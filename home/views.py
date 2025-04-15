from django.shortcuts import render
from books.models import Book, Category
from django.db.models import Avg

def home(request):
    # Featured books
    featured_books = Book.objects.all().annotate(avg_rating=Avg('reviews__rating')).order_by('-created_at')[:6]
    
    # Top categories
    categories = Category.objects.filter(parent__isnull=True)[:6]
    
    # Best-selling books
    bestsellers = Book.objects.all().annotate(avg_rating=Avg('reviews__rating')).order_by('?')[:6]
    
    context = {
        'featured_books': featured_books,
        'categories': categories,
        'bestsellers': bestsellers
    }
    return render(request, 'home/index.html', context)