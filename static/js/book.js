
document.addEventListener('DOMContentLoaded', function() {
    
    const addToCartButton = document.querySelector('.js-add-to-cart');
    if (addToCartButton) {
        addToCartButton.addEventListener('click', () => {
            const bookId = addToCartButton.dataset.bookId;
            addToCart(bookId);
            
            
            showNotification("Livro adicionado ao carrinho");
        });
    }

    // Add event listeners for review form if it exists
    const reviewForm = document.getElementById('review-form');
    if (reviewForm) {
        reviewForm.addEventListener('submit', function(event) {
            event.preventDefault();
            
            
            const formData = new FormData(this);
            
            
            fetch(this.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Clear the form
                    this.reset();
                    
                    // Refresh the page to show the new review
                    window.location.reload();
                } else {
                    showNotification(data.error || "Erro ao enviar avaliação", "error");
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showNotification("Erro ao enviar avaliação", "error");
            });
        });
    }

    // Handle add to wishlist button if it exists
    const wishlistButton = document.querySelector('.js-add-to-wishlist');
    if (wishlistButton) {
        wishlistButton.addEventListener('click', () => {
            const bookId = wishlistButton.dataset.bookId;
            
            fetch('/users/wishlist/add/', {  // Add the /users/ prefix
                method: 'POST',
                body: JSON.stringify({ book_id: bookId }),
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCsrfToken(),
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showNotification("Livro adicionado aos favoritos");
                    
                    // Update the button
                    wishlistButton.innerHTML = '<i class="bi bi-heart-fill text-danger"></i> Adicionado aos Favoritos';
                    wishlistButton.disabled = true;
                } else {
                    showNotification(data.error || "Erro ao adicionar aos favoritos", "error");
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showNotification("Erro ao adicionar aos favoritos", "error");
            });
        });
    }

    // Cart icon click handler
    const cartIcon = document.querySelector('.js-bi-cart');
    if (cartIcon) {
        cartIcon.addEventListener('click', (event) => {
            event.preventDefault();
            showCartOverlay();
        });
    }

    // Update cart count on page load
    updateCartCount();
});

// Helper function to get CSRF token
function getCsrfToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

// Function to show notifications
function showNotification(message, type = 'success') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} notification-toast`;
    notification.textContent = message;
    
    // Add to body
    document.body.appendChild(notification);
    
    // Show with animation
    setTimeout(() => {
        notification.classList.add('show');
    }, 10);
    
    // Hide after 3 seconds
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 3000);
}