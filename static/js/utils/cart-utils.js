// This is a simplified version - you'll need to adapt further as needed
const cart = JSON.parse(localStorage.getItem('cart')) || [];

// Format price from cents to currency
export function formatPrice(priceCents) {
  return (priceCents / 100).toLocaleString('pt-PT', {
    style: 'currency',
    currency: 'EUR'
  });
}

// Update cart count in the UI
// Update cart count in the UI
export function updateCartCount() {
  const cartCount = cart.reduce((acc, item) => acc + item.quantity, 0);
  const cartBadges = document.querySelectorAll('.js-cart-count');
  cartBadges.forEach(badge => {
    badge.textContent = cartCount;
  });
}

// Add item to cart
export function addToCart(bookId) {
  let matchingBook = cart.find(item => item.bookId === bookId);
  
  if (matchingBook) {
    matchingBook.quantity += 1;
  } else {
    cart.push({
      bookId: bookId,
      quantity: 1
    });
  }
  
  localStorage.setItem('cart', JSON.stringify(cart));
  updateCartCount();
  
  // Show notification
  showNotification('Livro adicionado ao carrinho com sucesso.');
}

// Remove item from cart
export function removeFromCart(bookId) {
  const bookIndex = cart.findIndex(item => item.bookId === bookId);
  
  if (bookIndex !== -1) {
    if (cart[bookIndex].quantity > 1) {
      cart[bookIndex].quantity -= 1;
    } else {
      cart.splice(bookIndex, 1);
    }
    
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
    
    // Update cart overlay if it's open
    const cartOverlay = document.querySelector('.cart-overlay');
    if (cartOverlay) {
      updateCartDisplay();
    }
    
    return true;
  }
  
  return false;
}

// Generate cart HTML - modified for Django
export function generateCartHTML() {
  if (cart.length === 0) {
    return `<div class="empty-cart-message">Seu carrinho está vazio</div>`;
  }
  
  let cartHTML = '<ul class="cart-items">';
  let totalCents = 0;
  
  cart.forEach(item => {
    // Note: In a real Django app, you'd fetch book data from the server
    // This is a simplified version that we'll replace later
    cartHTML += `
      <li class="cart-item" data-book-id="${item.bookId}">
        <div class="cart-item-info">
          <div class="cart-item-details">
            <h6 class="cart-item-title">Livro ID: ${item.bookId}</h6>
            <div class="cart-item-price">Quantidade: ${item.quantity}</div>
          </div>
        </div>
        <div class="cart-item-actions">
          <button class="btn btn-sm btn-outline-danger js-remove-from-cart" data-book-id="${item.bookId}">
            <i class="bi bi-dash"></i>
          </button>
          <button class="btn btn-sm btn-outline-primary js-add-to-cart" data-book-id="${item.bookId}">
            <i class="bi bi-plus"></i>
          </button>
        </div>
      </li>
    `;
  });
  
  cartHTML += `
    </ul>
    <div class="cart-actions">
      <a href="/checkout/" class="btn btn-success w-100">Finalizar Compra</a>
    </div>
  `;
  
  return cartHTML;
}

// Create and display cart overlay
export function showCartOverlay() {
  // Remove existing overlay if it exists
  const existingOverlay = document.querySelector('.cart-overlay');
  if (existingOverlay) {
    existingOverlay.remove();
    return;
  }
  
  // Create overlay
  const overlay = document.createElement('div');
  overlay.className = 'cart-overlay';
  overlay.innerHTML = `
    <div class="cart-overlay-content">
      <div class="cart-overlay-header">
        <h5>Seu Carrinho</h5>
        <button class="btn-close js-close-cart"></button>
      </div>
      <div class="cart-overlay-body">
        ${generateCartHTML()}
      </div>
    </div>
  `;
  
  document.body.appendChild(overlay);
  
  // Add event listeners
  document.querySelector('.js-close-cart').addEventListener('click', () => {
    overlay.remove();
  });
  
  // Close when clicking outside of the cart
  overlay.addEventListener('click', (e) => {
    if (e.target === overlay) {
      overlay.remove();
    }
  });
  
  // Add event listeners for cart buttons
  const addButtons = overlay.querySelectorAll('.js-add-to-cart');
  const removeButtons = overlay.querySelectorAll('.js-remove-from-cart');
  
  addButtons.forEach(button => {
    button.addEventListener('click', () => {
      const bookId = button.dataset.bookId;
      addToCart(bookId);
      updateCartDisplay();
    });
  });
  
  removeButtons.forEach(button => {
    button.addEventListener('click', () => {
      const bookId = button.dataset.bookId;
      removeFromCart(bookId);
      updateCartDisplay();
    });
  });
}

// Update the cart overlay contents
function updateCartDisplay() {
  const cartBody = document.querySelector('.cart-overlay-body');
  if (cartBody) {
    cartBody.innerHTML = generateCartHTML();
    
    // Re-add event listeners
    const addButtons = cartBody.querySelectorAll('.js-add-to-cart');
    const removeButtons = cartBody.querySelectorAll('.js-remove-from-cart');
    
    addButtons.forEach(button => {
      button.addEventListener('click', () => {
        const bookId = button.dataset.bookId;
        addToCart(bookId);
        updateCartDisplay();
      });
    });
    
    removeButtons.forEach(button => {
      button.addEventListener('click', () => {
        const bookId = button.dataset.bookId;
        removeFromCart(bookId);
        updateCartDisplay();
      });
    });
  }
}

// Show notification
function showNotification(message) {
  // Create notification element
  const notification = document.createElement('div');
  notification.className = 'cart-notification';
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

// Initialize cart on page load
document.addEventListener('DOMContentLoaded', function() {
  updateCartCount();
  
  // Add cart icon click handler
  const cartIcon = document.querySelector('.js-bi-cart');
  if (cartIcon) {
    cartIcon.addEventListener('click', (event) => {
      event.preventDefault();
      showCartOverlay();
    });
  }
  
  // Add event listeners for add to cart buttons
  document.querySelectorAll('.js-add-to-cart').forEach(button => {
    button.addEventListener('click', () => {
      const bookId = button.dataset.bookId;
      addToCart(bookId);
    });
  });
});