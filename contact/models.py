from django.db import models
from django.contrib.auth.models import User

class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ('general', 'Informação Geral'),
        ('order', 'Dúvida sobre Pedido'),
        ('book', 'Sugestão de Livro'),
        ('technical', 'Problema Técnico'),
        ('other', 'Outro Assunto'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, verbose_name='Assunto')
    message = models.TextField(verbose_name='Mensagem')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Utilizador')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Envio')
    is_read = models.BooleanField(default=False, verbose_name='Lida')
    
    class Meta:
        verbose_name = 'Mensagem de Contato'
        verbose_name_plural = 'Mensagens de Contato'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.name} - {self.get_subject_display()}'
