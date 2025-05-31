# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada com sucesso para {username}! Agora você pode entrar.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def orders(request):
    return render(request, 'users/orders.html')

@login_required
def wishlist(request):
    from .models import Wishlist
    wishlist_items = Wishlist.objects.filter(user=request.user).select_related('book')
    return render(request, 'users/wishlist.html', {'wishlist_items': wishlist_items})

@csrf_exempt
@login_required
def add_to_wishlist(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            book_id = data.get('book_id')
            
            if not book_id:
                return JsonResponse({
                    'success': False,
                    'error': 'ID do livro não fornecido'
                })
            
            # Import the models
            from books.models import Book
            from .models import Wishlist
            
            try:
                book = Book.objects.get(id=book_id)
                
                # Check if book is already in wishlist
                if Wishlist.objects.filter(user=request.user, book=book).exists():
                    return JsonResponse({
                        'success': False,
                        'error': 'Livro já está na lista de desejos'
                    })
                
                # Add to wishlist
                Wishlist.objects.create(user=request.user, book=book)
                
                return JsonResponse({
                    'success': True,
                    'message': f'"{book.title}" adicionado à lista de desejos!'
                })
                
            except Book.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'error': 'Livro não encontrado'
                })
            
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'error': 'Dados inválidos'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': f'Erro interno: {str(e)}'
            })
    
    return JsonResponse({'success': False, 'error': 'Método não permitido'})

@login_required
def remove_from_wishlist(request, book_id):
    if request.method == 'POST':
        try:
            from .models import Wishlist
            wishlist_item = Wishlist.objects.get(user=request.user, book_id=book_id)
            book_title = wishlist_item.book.title
            wishlist_item.delete()
            messages.success(request, f'"{book_title}" removido da lista de desejos.')
        except Wishlist.DoesNotExist:
            messages.error(request, 'Livro não encontrado na lista de desejos.')
        except Exception as e:
            messages.error(request, f'Erro ao remover livro: {str(e)}')
    
    return redirect('wishlist')

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        messages.success(request, 'Você foi desconectado com sucesso.')
        return redirect('home')
    
    return redirect('home')