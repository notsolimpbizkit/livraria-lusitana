from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='subcategories')
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])

class Book(models.Model):
    isbn = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    synopsis = models.TextField()
    price_cents = models.IntegerField()
    currency = models.CharField(max_length=3, default='EUR')
    publication_date = models.DateField()
    publisher = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=100, blank=True, null=True)
    binding_type = models.CharField(max_length=50)
    pages = models.IntegerField()
    image = models.ImageField(upload_to='books/', blank=True, null=True)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])
        
    def formatted_price(self):
        return f"€{self.price_cents/100:.2f}"

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('book', 'user')
        
    def __str__(self):
        return f"{self.user.username}'s review of {self.book.title}"