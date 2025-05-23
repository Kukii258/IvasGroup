// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  console.log('Ivas Group Website Loaded');

  // Initialize Swiper slider
  const swiper = new Swiper('.swiper', {
    // Optional parameters
    loop: true,
    effect: 'fade',
    speed: 1000,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
    },

    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },

    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });

  // Mobile menu toggle
  const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
  const nav = document.querySelector('nav');
  const navLinks = document.querySelectorAll('nav a');

  if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      nav.classList.toggle('active');

      // Toggle icon between bars and times
      const icon = this.querySelector('i');
      if (icon.classList.contains('fa-bars')) {
        icon.classList.remove('fa-bars');
        icon.classList.add('fa-times');
      } else {
        icon.classList.remove('fa-times');
        icon.classList.add('fa-bars');
      }
    });
  }

  // Close mobile menu when clicking outside
  document.addEventListener('click', function(e) {
    if (nav.classList.contains('active') && !nav.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
      nav.classList.remove('active');
      const icon = mobileMenuBtn.querySelector('i');
      icon.classList.remove('fa-times');
      icon.classList.add('fa-bars');
    }
  });

  // Handle mobile menu link clicks
  navLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      // Only prevent default if it's a hash link
      if (this.getAttribute('href').startsWith('#')) {
        e.preventDefault();
      }

      // Close mobile menu
      if (nav.classList.contains('active')) {
        nav.classList.remove('active');
        const icon = mobileMenuBtn.querySelector('i');
        icon.classList.remove('fa-times');
        icon.classList.add('fa-bars');
      }

      // Handle smooth scrolling for hash links
      if (this.getAttribute('href').startsWith('#')) {
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);

        if (targetElement) {
          const headerHeight = document.querySelector('header').offsetHeight;
          const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight;

          window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
          });
        }
      }
    });
  });

  // Header scroll effect
  const header = document.querySelector('header');

  function handleHeaderScroll() {
    if (window.scrollY > 100) {
      header.style.background = 'rgba(5, 5, 5, 0.95)';
      header.style.boxShadow = '0 5px 20px rgba(0, 0, 0, 0.5)';
    } else {
      header.style.background = 'rgba(10, 10, 10, 0.9)';
      header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.3)';
    }
  }

  window.addEventListener('scroll', handleHeaderScroll);

  // Form submission handling
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();

      // Get form values
      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      const message = document.getElementById('message').value;

      // Simple validation
      if (!name || !email || !message) {
        alert('Please fill in all required fields.');
        return;
      }

      // In a real application, you would send this data to a server
      console.log('Form submitted:', { name, email, message });

      // Show success message
      alert('Thank you for your message! We will get back to you soon.');

      // Reset form
      contactForm.reset();
    });
  }

  // Animate spotlight effects
  function animateSpotlights() {
    const spotlights = document.querySelectorAll('.spotlight');

    spotlights.forEach(spotlight => {
      // Random movement within viewport boundaries
      const randomX = Math.random() * window.innerWidth;
      const randomY = Math.random() * window.innerHeight;

      spotlight.style.transition = 'transform 20s ease-in-out';
      spotlight.style.transform = `translate(${randomX}px, ${randomY}px)`;
    });
  }

  // Initial animation
  animateSpotlights();

  // Continue animation at intervals
  setInterval(animateSpotlights, 20000);


  const filterButtons = document.querySelectorAll('.filter-btn');
  const galleryItems = document.querySelectorAll('.gallery-item');

  if (filterButtons.length > 0 && galleryItems.length > 0) {
    filterButtons.forEach(button => {
      button.addEventListener('click', function() {
        // Remove active class from all buttons
        filterButtons.forEach(btn => btn.classList.remove('active'));

        // Add active class to clicked button
        this.classList.add('active');

        const filterValue = this.getAttribute('data-filter');

        galleryItems.forEach(item => {
          if (filterValue === 'all' || item.getAttribute('data-category').includes(filterValue)) {
            item.style.display = 'block';
          } else {
            item.style.display = 'none';
          }
        });
      });
    });
  }


    const galleryElement = document.getElementById('lightgallery');
  if (galleryElement) {
    lightGallery(galleryElement, {
      plugins: [lgZoom, lgThumbnail],
      speed: 500,
      download: false,
      counter: true,
      enableSwipe: true,
      enableDrag: true,
      swipeThreshold: 50,
      mode: 'lg-fade',
      thumbnail: true,
      animateThumb: true,
      showThumbByDefault: false,
      thumbWidth: 100,
      thumbHeight: '80px',
      thumbMargin: 5
    });
  }




/*
      document.addEventListener('DOMContentLoaded', function() {
        // Language switcher functionality
        const languageButtons = document.querySelectorAll('.language-btn');

        function switchLanguage(lang) {
          // Update all translatable elements
          document.querySelectorAll('[data-' + lang + ']').forEach(element => {
            element.textContent = element.getAttribute('data-' + lang);
          });

          // Update button states
          languageButtons.forEach(btn => {
            btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
          });
        }

        languageButtons.forEach(btn => {
          btn.addEventListener('click', function() {
            const lang = this.getAttribute('data-lang');
            switchLanguage(lang);
          });
        });
      });

});

// Language buttons
document.addEventListener('DOMContentLoaded', function() {
  const languageButtons = document.querySelectorAll('.language-btn');

  function switchLanguage(lang) {
    // Update all translatable elements
    document.querySelectorAll('[data-' + lang + ']').forEach(element => {
      element.textContent = element.getAttribute('data-' + lang);
    });

    // Update button states
    languageButtons.forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    });

    // Store the selected language in local storage
    localStorage.setItem('selectedLanguage', lang);
  }

  // Load the stored language preference, or default to English
  const storedLanguage = localStorage.getItem('selectedLanguage') || 'en';
  switchLanguage(storedLanguage);

  languageButtons.forEach(btn => {
    btn.addEventListener('click', function() {
      const lang = this.getAttribute('data-lang');
      switchLanguage(lang);
    });
  });

 */
});

