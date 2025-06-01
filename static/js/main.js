
document.addEventListener('DOMContentLoaded', function() {
    

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


// We're just declaring them here for reference
function addToCart(bookId) {
    //cart-utils.js
}

function showCartOverlay() {
    //cart-utils.js
}

function updateCartCount() {
    //cart-utils.js
}