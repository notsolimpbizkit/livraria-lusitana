// File path: static/js/checkout.js
document.addEventListener('DOMContentLoaded', function() {
  // Get cart items from localStorage
  const cart = JSON.parse(localStorage.getItem('cart')) || [];
  
  // Store cart in hidden field for form submission
  const cartItemsInput = document.getElementById('cart-items-input');
  if (cartItemsInput) {
      cartItemsInput.value = JSON.stringify(cart);
  }
  
  // Fetch book details for cart items
  fetch('/api/cart/', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCsrfToken(),
          'X-Requested-With': 'XMLHttpRequest'
      },
      body: JSON.stringify({ items: cart })
  })
  .then(response => response.json())
  .then(data => {
      const checkoutSummary = document.querySelector('.js-checkout-summary');
      if (!checkoutSummary) return;
      
      if (data.items && data.items.length > 0) {
          // Render cart items
          let checkoutHtml = '';
          
          data.items.forEach(item => {
              checkoutHtml += `
                  <li class="list-group-item d-flex justify-content-between">
                  <div>
                      <span>${item.title}</span>
                      <small class="text-muted d-block">Quantidade: ${item.quantity}</small>
                  </div>
                  <strong>${formatPrice(item.subtotal_cents)}</strong>
                  </li>
              `;
          });
  
          // Add total
          checkoutHtml += `
              <li class="list-group-item d-flex justify-content-between bg-light">
                      <span><strong>Total:</strong></span>
                      <strong>${data.formatted_total}</strong>
              </li>
          `;
          
          checkoutSummary.innerHTML = checkoutHtml;
      } else {
          // Empty cart
          checkoutSummary.innerHTML = `
              <li class="list-group-item text-center py-5">
                  <p>Seu carrinho está vazio</p>
                  <a href="/" class="btn btn-primary mt-3">Continuar Comprando</a>
              </li>
          `;
      }
  })
  .catch(error => {
      console.error('Error:', error);
      const checkoutSummary = document.querySelector('.js-checkout-summary');
      if (checkoutSummary) {
          checkoutSummary.innerHTML = `
              <li class="list-group-item text-center py-5">
                  <p class="text-danger">Erro ao carregar itens do carrinho</p>
                  <a href="/" class="btn btn-primary mt-3">Voltar para a Loja</a>
              </li>
          `;
      }
  });
  
  // Handle form submission
  const checkoutForm = document.getElementById('checkout-form');
  if (checkoutForm) {
      checkoutForm.addEventListener('submit', function(event) {
          event.preventDefault();
          
          // Show loading state
          const submitButton = this.querySelector('button[type="submit"]');
          const originalText = submitButton.textContent;
          submitButton.disabled = true;
          submitButton.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Processando...';
          
          // Get form data
          const formData = new FormData(this);
          
          // Send the order
          fetch(this.action, {
              method: 'POST',
              body: formData,
              headers: {
                  'X-Requested-With': 'XMLHttpRequest'
              }
          })
          .then(response => response.json())
          .then(data => {
              if (data.success) {
                  // Clear cart
                  localStorage.removeItem('cart');
                  
                  // Redirect to confirmation page
                  window.location.href = data.redirect_url;
              } else {
                  // Show error
                  alert(data.error || "Ocorreu um erro ao processar o pedido.");
                  
                  // Reset button
                  submitButton.disabled = false;
                  submitButton.innerHTML = originalText;
              }
          })
          .catch(error => {
              console.error('Error:', error);
              
              // Show error
              alert("Ocorreu um erro ao processar o pedido. Por favor, tente novamente.");
              
              // Reset button
              submitButton.disabled = false;
              submitButton.innerHTML = originalText;
          });
      });
  }
  
  // Update cart count
  updateCartCount();
});

// Helper function to get CSRF token
function getCsrfToken() {
  return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

// Helper function to format price (can be replaced by the one from cart-utils.js)
function formatPrice(priceCents) {
  return (priceCents / 100).toLocaleString('pt-PT', {
      style: 'currency',
      currency: 'EUR'
  });
}