from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from books.models import Book

@csrf_exempt
@require_http_methods(["POST"])
def get_cart_items(request):
    try:
        data = json.loads(request.body)
        cart_items = data.get('items', [])              
        
        # Process cart items
        cart_data = []
        total_cents = 0
        
        for item in cart_items:
            book_id = item.get('bookId')
            quantity = item.get('quantity', 1)
            
            try:
                book = Book.objects.get(id=book_id)
                item_data = {
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
                    'price_cents': book.price_cents,
                    'image_url': book.image.url if book.image else None,
                    'quantity': quantity,
                    'subtotal_cents': book.price_cents * quantity
                }
                cart_data.append(item_data)
                total_cents += item_data['subtotal_cents']
            except Book.DoesNotExist:
                pass
        
        return JsonResponse({
            'items': cart_data,
            'total_cents': total_cents,
            'formatted_total': f"€{total_cents/100:.2f}"
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)