from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Avg
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book, Category, Review
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
@csrf_exempt
def get_cart_books(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cart_items = data.get('cart', [])
            
            books_data = []
            total = 0
            
            for item in cart_items:
                try:
                    # Convert string ID to integer
                    book_id = int(item['bookId'])
                    book = Book.objects.get(id=book_id)
                    
                    # Use price_cents instead of price
                    price = book.price_cents / 100  # Convert cents to euros
                    subtotal = price * item['quantity']
                    total += subtotal
                    
                    books_data.append({
                        'id': book.id,
                        'title': book.title,
                        'price': price,
                        'formatted_price': f"€{price:.2f}",  # Format price manually
                        'quantity': item['quantity'],
                        'subtotal': subtotal
                    })
                except (Book.DoesNotExist, ValueError, KeyError) as e:
                    print(f"Error processing item {item}: {e}")
                    continue
            
            return JsonResponse({
                'books': books_data,
                'total': total,
                'formatted_total': f"€{total:.2f}"
            })
        except Exception as e:
            print(f"Cart API Error: {e}")
            return JsonResponse({'error': str(e)})
    
    return JsonResponse({'error': 'Invalid method'})

def book_list(request):
    # Get base queryset
    books = Book.objects.all()
    
    # Calculate average rating for each book
    for book in books:
        reviews = book.reviews.all()
        if reviews.exists():
            total_rating = sum([review.rating for review in reviews])
            book.avg_rating = total_rating / reviews.count()
        else:
            book.avg_rating = 0
    
    # Get all top-level categories
    categories = Category.objects.filter(parent__isnull=True)
    
    # Apply filters
    category_id = request.GET.get('category')
    price_range = request.GET.get('price')
    sort_by = request.GET.get('sort', 'title')
    
    # Filter by category
    if category_id:
        try:
            category = Category.objects.get(pk=category_id)
            subcategories = Category.objects.filter(parent=category)
            books = [book for book in books if book.category == category or book.category in subcategories]
        except Category.DoesNotExist:
            pass
    
    # Filter by price range
    if price_range:
        if price_range == 'under10':
            books = [book for book in books if book.price_cents < 1000]
        elif price_range == '10to20':
            books = [book for book in books if 1000 <= book.price_cents < 2000]
        elif price_range == '20to30':
            books = [book for book in books if 2000 <= book.price_cents < 3000]
        elif price_range == 'over30':
            books = [book for book in books if book.price_cents >= 3000]
    
    # Sort books
    if sort_by == 'price_asc':
        books = sorted(books, key=lambda x: x.price_cents)
    elif sort_by == 'price_desc':
        books = sorted(books, key=lambda x: x.price_cents, reverse=True)
    elif sort_by == 'title':
        books = sorted(books, key=lambda x: x.title)
    elif sort_by == 'newest':
        books = sorted(books, key=lambda x: x.publication_date, reverse=True)
    elif sort_by == 'rating':
        books = sorted(books, key=lambda x: x.avg_rating, reverse=True)
    
    context = {
        'books': books,
        'categories': categories,
        'selected_category_id': category_id,
        'selected_price_range': price_range,
        'selected_sort': sort_by
    }
    return render(request, 'books/book_list.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    # Calculate average rating manually to ensure it's always available
    reviews = book.reviews.all().order_by('-created_at')
    
    # Calculate average rating
    if reviews.exists():
        total_rating = sum([review.rating for review in reviews])
        book.avg_rating = total_rating / reviews.count()
    else:
        book.avg_rating = 0
    
    # Check if user has already reviewed this book
    user_review = None
    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()
    
    # Get related books (same category or author)
    related_books = Book.objects.filter(
        Q(category=book.category) | Q(author=book.author)
    ).exclude(pk=book.pk)
    
    # Calculate avg rating for related books too
    for related_book in related_books:
        related_reviews = related_book.reviews.all()
        if related_reviews.exists():
            total_rating = sum([review.rating for review in related_reviews])
            related_book.avg_rating = total_rating / related_reviews.count()
        else:
            related_book.avg_rating = 0
    
    related_books = related_books[:4]
    
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

@login_required
def add_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        try:
            rating = int(request.POST.get('rating', 0))
            review_text = request.POST.get('review_text', '').strip()
            
            # Validate rating
            if not (1 <= rating <= 5):
                messages.error(request, 'A avaliação deve ser entre 1 e 5 estrelas.')
                return redirect('book_detail', pk=book_id)
            
            # Validate review text
            if not review_text:
                messages.error(request, 'Por favor, escreva um comentário sobre o livro.')
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
            
        except ValueError:
            messages.error(request, 'Dados de avaliação inválidos.')
        except Exception as e:
            messages.error(request, 'Ocorreu um erro ao processar sua avaliação. Tente novamente.')
        
        return redirect('book_detail', pk=book_id)
    
    return redirect('book_detail', pk=book_id)