from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from books.models import Book
from orders.models import Order, OrderItem
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json

@login_required
def checkout(request):
    """Display checkout page"""
    context = {
        'paypal_client_id': settings.PAYPAL_CLIENT_ID,
        'paypal_environment': settings.PAYPAL_ENVIRONMENT,
    }
    return render(request, 'checkout/checkout.html', context)

@login_required
def process_order(request):
    if request.method == 'POST':
        try:
            # Parse the cart items from POST
            cart_items = json.loads(request.POST.get('cart_items', '[]'))
            
            # Get shipping information
            shipping_address = request.POST.get('address', '')
            shipping_city = request.POST.get('city', '')
            shipping_postal_code = request.POST.get('postal_code', '')
            payment_method = request.POST.get('payment_method', '')
            
            if not cart_items or not shipping_address or not shipping_city or not shipping_postal_code:
                return JsonResponse({'error': 'Informações incompletas'}, status=400)
            
            # Calculate total
            total_cents = 0
            validated_items = []
            
            for item in cart_items:
                book_id = item.get('bookId')
                quantity = int(item.get('quantity', 1))
                
                try:
                    book = Book.objects.get(id=book_id)
                    if book.stock >= quantity:
                        item_total = book.price_cents * quantity
                        total_cents += item_total
                        validated_items.append({
                            'book': book,
                            'quantity': quantity,
                            'price_cents': book.price_cents
                        })
                    else:
                        return JsonResponse({'error': f'Estoque insuficiente para {book.title}'}, status=400)
                except Book.DoesNotExist:
                    return JsonResponse({'error': 'Livro não encontrado'}, status=400)
            
            # Create order
            order = Order(
                user=request.user,
                total_amount_cents=total_cents,
                shipping_address=shipping_address,
                shipping_city=shipping_city,
                shipping_postal_code=shipping_postal_code,
                payment_method=payment_method,
                status='pending'
            )
            order.save()
            
            # Create order items and update stock
            for item in validated_items:
                OrderItem.objects.create(
                    order=order,
                    book=item['book'],
                    quantity=item['quantity'],
                    price_at_order_cents=item['price_cents']
                )
                
                # Update stock
                book = item['book']
                book.stock -= item['quantity']
                book.save()
            
            return JsonResponse({
                'success': True,
                'order_id': order.id,
                'redirect_url': f'/orders/{order.id}/confirmation/'
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Método não permitido'}, status=405)

@csrf_exempt
def process_paypal_payment(request):
    """Process PayPal payment"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Get payment details from PayPal
            payment_id = data.get('payment_id')
            payer_id = data.get('payer_id')
            amount = data.get('amount')
            cart_items = data.get('cart_items', [])
            
            # Here you would:
            # 1. Verify the payment with PayPal API (optional but recommended)
            # 2. Create order in your database
            # 3. Clear the cart
            # 4. Send confirmation email
            
            # For now, let's just create a simple response
            order_id = f"ORDER-{payment_id[-8:]}"  # Simple order ID generation
            
            return JsonResponse({
                'success': True,
                'order_id': order_id,
                'message': 'Payment processed successfully!'
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'success': False, 'error': 'Invalid method'})