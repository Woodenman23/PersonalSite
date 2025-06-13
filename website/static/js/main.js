/**
 * Main JavaScript file for portfolio site
 * Handles global functionality and initialization
 */

document.addEventListener('DOMContentLoaded', function() {
  console.log('Portfolio site initialized');
  
  // Initialize smooth scrolling for anchor links
  initSmoothScrolling();
  
  // Initialize tab persistence (remember which tab was active)
  initTabPersistence();
  
  // Initialize any animations or effects
  initAnimations();
});

/**
 * Smooth scrolling for anchor links
 */
function initSmoothScrolling() {
  const anchorLinks = document.querySelectorAll('a[href^="#"]');
  
  anchorLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      const target = document.querySelector(href);
      
      if (target && href !== '#') {
        e.preventDefault();
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
}

/**
 * Remember active tab across page reloads
 */
function initTabPersistence() {
  // Get active tab from localStorage
  const activeTab = localStorage.getItem('activeTab');
  
  if (activeTab) {
    const tabElement = document.querySelector(`a[href="${activeTab}"]`);
    if (tabElement && typeof $ !== 'undefined') {
      $(tabElement).tab('show');
    }
  }
  
  // Save active tab when clicked
  const tabLinks = document.querySelectorAll('[data-toggle="tab"]');
  tabLinks.forEach(tab => {
    tab.addEventListener('click', function() {
      const href = this.getAttribute('href');
      localStorage.setItem('activeTab', href);
    });
  });
}

/**
 * Initialize subtle animations and effects
 */
function initAnimations() {
  // Add fade-in effect for achievement cards
  const cards = document.querySelectorAll('.achievement-card');
  
  // Intersection Observer for scroll animations
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
        }
      });
    }, {
      threshold: 0.1
    });
    
    cards.forEach(card => {
      card.style.opacity = '0';
      card.style.transform = 'translateY(20px)';
      card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
      observer.observe(card);
    });
  }
}

/**
 * Utility function for debouncing
 */
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}