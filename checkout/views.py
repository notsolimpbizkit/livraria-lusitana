from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from books.models import Book
from orders.models import Order, OrderItem  # Import from orders app
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

@csrf_exempt
@login_required
def process_paypal_payment(request):
    """Process PayPal payment"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Get payment details from PayPal
            payment_id = data.get('payment_id')
            payer_id = data.get('payer_id')
            amount = float(data.get('amount', 0))
            cart_items = data.get('cart_items', [])
            paypal_details = data.get('paypal_details', {})
            shipping_data = data.get('shipping_data', {})  # New: Get shipping data
            
            if not cart_items:
                return JsonResponse({
                    'success': False,
                    'error': 'Carrinho vazio'
                })
            
            # Convert EUR amount to cents for storage
            total_amount_cents = int(amount * 100)
            
            # Validate cart items and calculate total
            validated_items = []
            calculated_total_cents = 0
            
            for item in cart_items:
                book_id = item.get('bookId') or item.get('book_id')
                quantity = int(item.get('quantity', 1))
                
                try:
                    book = Book.objects.get(id=book_id)
                    if book.stock >= quantity:
                        item_total_cents = book.price_cents * quantity
                        calculated_total_cents += item_total_cents
                        validated_items.append({
                            'book': book,
                            'quantity': quantity,
                            'price_cents': book.price_cents
                        })
                    else:
                        return JsonResponse({
                            'success': False,
                            'error': f'Estoque insuficiente para {book.title}'
                        })
                except Book.DoesNotExist:
                    return JsonResponse({
                        'success': False,
                        'error': f'Livro com ID {book_id} não encontrado'
                    })
            
            # Verify amount matches (with small tolerance for floating point)
            if abs(calculated_total_cents - total_amount_cents) > 5:  # 5 cents tolerance
                return JsonResponse({
                    'success': False,
                    'error': 'Valor do pagamento não confere com o carrinho'
                })
            
            # Create the order in database with real shipping info
            order = Order.objects.create(
                user=request.user,
                total_amount_cents=total_amount_cents,
                payment_method='paypal',
                status='processing',  # Since PayPal payment was successful
                shipping_address=shipping_data.get('address', f"PayPal Payment ID: {payment_id}"),
                shipping_city=shipping_data.get('city', 'Lisboa'),
                shipping_postal_code=shipping_data.get('postalCode', '1000-001'),
            )
            
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
            
            # Optionally save address to user profile
            if shipping_data.get('saveAddress', False):
                try:
                    from users.models import UserProfile
                    profile, created = UserProfile.objects.get_or_create(user=request.user)
                    profile.address = shipping_data.get('address', '')
                    profile.city = shipping_data.get('city', '')
                    profile.postal_code = shipping_data.get('postalCode', '')
                    profile.phone = shipping_data.get('phone', '')
                    profile.save()
                except Exception as profile_error:
                    print(f"Error saving profile: {profile_error}")
                    # Don't fail the order if profile save fails
            
            # Log successful order creation
            print(f"Order created successfully: ID {order.id}, User: {request.user.username}")
            
            return JsonResponse({
                'success': True,
                'order_id': order.id,  # Real database ID
                'message': f'Pagamento processado com sucesso! Pedido #{order.id}'
            })
            
        except Exception as e:
            print(f"Error in process_paypal_payment: {e}")
            return JsonResponse({
                'success': False,
                'error': f'Erro ao processar pagamento: {str(e)}'
            })
    
    return JsonResponse({'success': False, 'error': 'Método não permitido'})

@login_required
def my_orders(request):
    """Display user's orders"""
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'orders/my_orders.html', {'orders': orders})