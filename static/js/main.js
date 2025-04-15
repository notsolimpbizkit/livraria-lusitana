// File path: static/js/main.js
document.addEventListener('DOMContentLoaded', function() {
    // Import cart utilities - we'll handle this differently in Django
    // The cart utilities are imported via the base template

    // Add to cart functionality
    document.querySelectorAll('.js-add-to-cart').forEach((button) => {
        button.addEventListener('click', () => {
            const bookId = button.dataset.bookId;
            addToCart(bookId);
        });
    });

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

// These functions will be available from cart-utils.js which is loaded in the base template
// We're just declaring them here for reference
function addToCart(bookId) {
    // This is implemented in cart-utils.js
}

function showCartOverlay() {
    // This is implemented in cart-utils.js
}

function updateCartCount() {
    // This is implemented in cart-utils.js
}