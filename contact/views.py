from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, user=request.user)
        
        if form.is_valid():
            contact_message = form.save(commit=False)
            
            # Associate with user if logged in
            if request.user.is_authenticated:
                contact_message.user = request.user
            
            contact_message.save()
            
            messages.success(request, 'Sua mensagem foi enviada com sucesso! Entraremos em contato em breve.')
            return redirect('contact')
        else:
            messages.error(request, 'Erro ao enviar mensagem. Verifique os dados e tente novamente.')
    
    else:
        form = ContactForm(user=request.user)
    
    context = {
        'form': form
    }
    return render(request, 'contact/contact.html', context)