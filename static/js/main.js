document.addEventListener('DOMContentLoaded', function() {
    const menuIcon = document.querySelector('.menu-icon');
    const navItems = document.querySelector('.nav-items');
    const closeBtn = document.querySelector('.close-btn'); // Add close button selector
  
    menuIcon.addEventListener('click', function() {
      navItems.classList.toggle('active');
      closeBtn.style.display = navItems.classList.contains('active') ? 'block' : 'none'; // Show or hide close button based on navbar state
    });
  
    const navLinks = document.querySelectorAll(".nav-items li a");
    navLinks.forEach(function(navLink) {
      navLink.addEventListener("click", function() {
        navItems.classList.remove("active");
        closeBtn.style.display = 'none'; // Hide close button when navbar is closed by clicking a link
      });
    });
  
    closeBtn.addEventListener('click', function() { // Add click event listener to close button
      navItems.classList.remove('active');
      closeBtn.style.display = 'none'; // Hide close button when navbar is closed
    });
  
    document.addEventListener('click', function(event) {
      const targetElement = event.target;
      const isNavMenuOpen = navItems.classList.contains('active');
      const isClickedInsideNavbar = targetElement.closest('.navbar');
  
      if (isNavMenuOpen && !isClickedInsideNavbar && !targetElement.classList.contains('close-btn')) {
        navItems.classList.remove('active');
        closeBtn.style.display = 'none'; // Hide close button when navbar is closed by clicking outside
      }
    });
  });