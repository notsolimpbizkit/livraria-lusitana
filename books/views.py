from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Avg
from .models import Book, Category, Review

def book_list(request):
    books = Book.objects.all().annotate(avg_rating=Avg('reviews__rating'))
    categories = Category.objects.filter(parent__isnull=True)
    
    context = {
        'books': books,
        'categories': categories
    }
    return render(request, 'books/book_list.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Book.objects.annotate(avg_rating=Avg('reviews__rating')), pk=pk)
    reviews = book.reviews.all().order_by('-created_at')
    
    # Get related books (same category)
    related_books = Book.objects.filter(category=book.category).exclude(pk=book.pk)[:4]
    
    context = {
        'book': book,
        'reviews': reviews,
        'related_books': related_books
    }
    return render(request, 'books/book_detail.html', context)

def category_books(request, pk):
    category = get_object_or_404(Category, pk=pk)
    books = Book.objects.filter(category=category).annotate(avg_rating=Avg('reviews__rating'))
    
    # Get all categories for the sidebar
    categories = Category.objects.filter(parent__isnull=True)
    
    context = {
        'category': category,
        'books': books,
        'categories': categories
    }
    return render(request, 'books/category_books.html', context)

def search_books(request):
    query = request.GET.get('q', '')
    books = []
    
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | 
            Q(author__icontains=query) |
            Q(synopsis__icontains=query) |
            Q(isbn__icontains=query)
        ).annotate(avg_rating=Avg('reviews__rating'))
    
    context = {
        'books': books,
        'query': query
    }
    return render(request, 'books/search_results.html', context)