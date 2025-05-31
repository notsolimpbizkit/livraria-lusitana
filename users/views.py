# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout as auth_logout

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
    return render(request, 'users/wishlist.html')

@login_required
def remove_from_wishlist(request, book_id):
    if request.method == 'POST':
        try:
            wishlist_item = request.user.wishlist_items.get(book_id=book_id)
            wishlist_item.delete()
            messages.success(request, 'Livro removido da lista de desejos.')
        except Exception as e:
            messages.error(request, f'Erro ao remover livro: {str(e)}')
    
    return redirect('wishlist')

def logout(request):
    if request.method == 'POST':
        auth_logout(request)  # This actually logs the user out
        messages.success(request, 'Você foi desconectado com sucesso.')
        return redirect('logout')  # or wherever you want to redirect
    
    # If someone tries to access via GET, redirect to home
    return redirect('home')