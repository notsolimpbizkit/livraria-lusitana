document.addEventListener('DOMContentLoaded', function() {
  // Get cart items from localStorage!!!
  const cart = JSON.parse(localStorage.getItem('cart')) || [];
  
  const cartItemsInput = document.getElementById('cart-items-input');
  if (cartItemsInput) {
      cartItemsInput.value = JSON.stringify(cart);
  }
  
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
  
          checkoutHtml += `
              <li class="list-group-item d-flex justify-content-between bg-light">
                      <span><strong>Total:</strong></span>
                      <strong>${data.formatted_total}</strong>
              </li>
          `;
          
          checkoutSummary.innerHTML = checkoutHtml;
      } else {
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
  
  const checkoutForm = document.getElementById('checkout-form');
  if (checkoutForm) {
      checkoutForm.addEventListener('submit', function(event) {
          event.preventDefault();
          
          const submitButton = this.querySelector('button[type="submit"]');
          const originalText = submitButton.textContent;
          submitButton.disabled = true;
          submitButton.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Processando...';
          
          const formData = new FormData(this);
          
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
                  localStorage.removeItem('cart');
                  
                  window.location.href = data.redirect_url;
              } else {
                  alert(data.error || "Ocorreu um erro ao processar o pedido.");
                  
                  submitButton.disabled = false;
                  submitButton.innerHTML = originalText;
              }
          })
          .catch(error => {
              console.error('Error:', error);
              
              alert("Ocorreu um erro ao processar o pedido. Por favor, tente novamente.");
              
              submitButton.disabled = false;
              submitButton.innerHTML = originalText;
          });
      });
  }
  
  updateCartCount();
});

function getCsrfToken() {
  return document.querySelector('[name=csrfmiddlewaretoken]').value;
}


function formatPrice(priceCents) {
  return (priceCents / 100).toLocaleString('pt-PT', {
      style: 'currency',
      currency: 'EUR'
  });
}