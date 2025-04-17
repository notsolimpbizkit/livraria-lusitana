from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Avg
from .models import Book, Category, Review
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def book_detail(request, pk):
    book = get_object_or_404(Book.objects.annotate(avg_rating=Avg('reviews__rating')), pk=pk)
    reviews = book.reviews.all().order_by('-created_at')
    
    # Check if user has already reviewed this book
    user_review = None
    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()
    
    # Get related books (same category or author)
    related_books = Book.objects.filter(
        Q(category=book.category) | Q(author=book.author)
    ).exclude(pk=book.pk)[:4]
    
    context = {
        'book': book,
        'reviews': reviews,
        'related_books': related_books,
        'user_review': user_review
    }
    return render(request, 'books/book_detail.html', context)

def category_books(request, pk):
    category = get_object_or_404(Category, pk=pk)
    
    # Get books in this category and its subcategories
    subcategories = Category.objects.filter(parent=category)
    books = Book.objects.filter(
        Q(category=category) | Q(category__in=subcategories)
    ).annotate(avg_rating=Avg('reviews__rating'))
    
    # Apply sorting
    sort_by = request.GET.get('sort', 'title')
    
    if sort_by == 'price_asc':
        books = books.order_by('price_cents')
    elif sort_by == 'price_desc':
        books = books.order_by('-price_cents')
    elif sort_by == 'title':
        books = books.order_by('title')
    elif sort_by == 'newest':
        books = books.order_by('-publication_date')
    elif sort_by == 'rating':
        books = books.order_by('-avg_rating')
    
    # Get all categories for navigation
    categories = Category.objects.filter(parent__isnull=True)
    
    context = {
        'category': category,
        'books': books,
        'categories': categories,
        'selected_category_id': str(pk),
        'selected_sort': sort_by
    }
    return render(request, 'books/category_books.html', context)

def search_books(request):
    query = request.GET.get('q', '')
    books = []
    random_books = []
    
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | 
            Q(author__icontains=query) |
            Q(synopsis__icontains=query) |
            Q(isbn__icontains=query)
        ).annotate(avg_rating=Avg('reviews__rating'))
        
        # If no results, get some random books to suggest
        if not books:
            random_books = Book.objects.order_by('?')[:4]
    
    context = {
        'books': books,
        'query': query,
        'random_books': random_books
    }
    return render(request, 'books/search_results.html', context)

def book_list(request):
    # Get base queryset
    books = Book.objects.all().annotate(avg_rating=Avg('reviews__rating'))
    
    # Get all top-level categories
    categories = Category.objects.filter(parent__isnull=True)
    
    # Apply filters
    category_id = request.GET.get('category')
    price_range = request.GET.get('price')
    sort_by = request.GET.get('sort', 'title')  # Default sort by title
    
    # Filter by category
    if category_id:
        try:
            category = Category.objects.get(pk=category_id)
            # Include books from this category and its subcategories
            subcategories = Category.objects.filter(parent=category)
            books = books.filter(Q(category=category) | Q(category__in=subcategories))
        except Category.DoesNotExist:
            pass
    
    # Filter by price range
    if price_range:
        if price_range == 'under10':
            books = books.filter(price_cents__lt=1000)
        elif price_range == '10to20':
            books = books.filter(price_cents__gte=1000, price_cents__lt=2000)
        elif price_range == '20to30':
            books = books.filter(price_cents__gte=2000, price_cents__lt=3000)
        elif price_range == 'over30':
            books = books.filter(price_cents__gte=3000)
    
    # Sort books
    if sort_by == 'price_asc':
        books = books.order_by('price_cents')
    elif sort_by == 'price_desc':
        books = books.order_by('-price_cents')
    elif sort_by == 'title':
        books = books.order_by('title')
    elif sort_by == 'newest':
        books = books.order_by('-publication_date')
    elif sort_by == 'rating':
        books = books.order_by('-avg_rating')
    
    context = {
        'books': books,
        'categories': categories,
        'selected_category_id': category_id,
        'selected_price_range': price_range,
        'selected_sort': sort_by
    }
    return render(request, 'books/book_list.html', context)

@login_required
def add_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        rating = int(request.POST.get('rating', 0))
        review_text = request.POST.get('review_text', '')
        
        if not (1 <= rating <= 5):
            messages.error(request, 'A avaliação deve ser entre 1 e 5.')
            return redirect('book_detail', pk=book_id)
        
        # Check if user already reviewed this book
        existing_review = Review.objects.filter(book=book, user=request.user).first()
        
        if existing_review:
            # Update existing review
            existing_review.rating = rating
            existing_review.review_text = review_text
            existing_review.save()
            messages.success(request, 'Sua avaliação foi atualizada com sucesso!')
        else:
            # Create new review
            Review.objects.create(
                book=book,
                user=request.user,
                rating=rating,
                review_text=review_text
            )
            messages.success(request, 'Sua avaliação foi adicionada com sucesso!')
        
        return redirect('book_detail', pk=book_id)
    
    return redirect('book_detail', pk=book_id)