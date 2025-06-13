/**
 * Contact Form Handler
 * Manages the contact modal form submission via AJAX
 */

document.addEventListener('DOMContentLoaded', function() {
  const sendEmailBtn = document.getElementById('sendEmailBtn');
  
  if (sendEmailBtn) {
    sendEmailBtn.addEventListener('click', function() {
      const form = document.getElementById('contactForm');
      
      if (form && form.checkValidity()) {
        // Disable button and show loading state
        sendEmailBtn.disabled = true;
        sendEmailBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-1"></i>Sending...';
        
        const formData = {
          name: document.getElementById('senderName').value,
          email: document.getElementById('senderEmail').value,
          subject: document.getElementById('subject').value,
          message: document.getElementById('message').value
        };
        
        // Send email via AJAX
        fetch('/send-email', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            // Show success message
            showMessage('Email sent successfully! I\'ll get back to you soon.', 'success');
            
            // Close modal after a brief delay
            setTimeout(() => {
              if (typeof $ !== 'undefined') {
                $('#contactModal').modal('hide');
              }
              form.reset();
            }, 2000);
            
          } else {
            showMessage(data.error || 'Failed to send email. Please try again.', 'error');
          }
        })
        .catch(error => {
          console.error('Error:', error);
          showMessage('Failed to send email. Please try again.', 'error');
        })
        .finally(() => {
          // Reset button state
          sendEmailBtn.disabled = false;
          sendEmailBtn.innerHTML = '<i class="fas fa-paper-plane me-1"></i>Send Message';
        });
        
      } else if (form) {
        form.reportValidity();
      }
    });
  }
});

/**
 * Show success/error messages in the modal
 */
function showMessage(message, type) {
  // Remove any existing message
  const existingMessage = document.querySelector('.contact-message');
  if (existingMessage) {
    existingMessage.remove();
  }
  
  // Create new message element
  const messageDiv = document.createElement('div');
  messageDiv.className = `alert contact-message ${type === 'success' ? 'alert-success' : 'alert-danger'}`;
  messageDiv.innerHTML = `
    <i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-exclamation-circle'} me-2"></i>
    ${message}
  `;
  
  // Insert message at the top of modal body
  const modalBody = document.querySelector('#contactModal .modal-body');
  modalBody.insertBefore(messageDiv, modalBody.firstChild);
}

/**
 * Enhanced form validation
 */
function validateContactForm() {
  const requiredFields = ['senderName', 'senderEmail', 'subject', 'message'];
  let isValid = true;
  
  requiredFields.forEach(fieldId => {
    const field = document.getElementById(fieldId);
    if (field && !field.value.trim()) {
      field.classList.add('is-invalid');
      isValid = false;
    } else if (field) {
      field.classList.remove('is-invalid');
    }
  });
  
  return isValid;
}

/**
 * Email validation helper
 */
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}