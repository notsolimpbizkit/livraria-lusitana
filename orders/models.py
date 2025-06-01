from django.db import models
from django.contrib.auth.models import User
from books.models import Book

class Order(models.Model):
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('processamento', 'Processamento'),
        ('enviado', 'Enviado'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount_cents = models.IntegerField()
    shipping_address = models.CharField(max_length=255)
    shipping_city = models.CharField(max_length=100)
    shipping_postal_code = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Order {self.id} by {self.user.username} on {self.order_date.strftime('%Y-%m-%d')}"
    
    def formatted_total(self):
        if self.total_amount_cents is not None:
            return f"€{self.total_amount_cents/100:.2f}"
        return "€0.00"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price_at_order_cents = models.IntegerField()
    
    def __str__(self):
        return f"{self.quantity}x {self.book.title} in Order {self.order.id}"
    
    def line_total_cents(self):
        if self.price_at_order_cents is not None:
            return self.quantity * self.price_at_order_cents
        return 0
        
    def formatted_price(self):
        if self.price_at_order_cents is not None:
            return f"€{self.price_at_order_cents/100:.2f}"
        return "€0.00"
        
    def formatted_line_total(self):
        line_total = self.line_total_cents()
        return f"€{line_total/100:.2f}"