from django.shortcuts import render
from books.models import Book, Category
from django.db.models import Avg

def home(request):
    # Featured books
    featured_book_ids = [20, 21, 22, 25, 26, 30]
    featured_books = Book.objects.filter(id__in=featured_book_ids).annotate(avg_rating=Avg('reviews__rating'))
    featured_books = sorted(featured_books, key=lambda x: featured_book_ids.index(x.id))
    
    # Top categories
    categories = Category.objects.filter(parent__isnull=True)[:6]
    
    # Best-selling books
    bestseller_ids = [28, 29, 26, 22, 24, 23]
    bestsellers = Book.objects.filter(id__in=bestseller_ids).annotate(avg_rating=Avg('reviews__rating'))
    bestsellers = sorted(bestsellers, key=lambda x: bestseller_ids.index(x.id))
    
    context = {
        'featured_books': featured_books,
        'categories': categories,
        'bestsellers': bestsellers
    }
    return render(request, 'home/index.html', context)