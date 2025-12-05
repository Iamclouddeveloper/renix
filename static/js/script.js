document.addEventListener("DOMContentLoaded", function () {
    const containers = document.querySelectorAll('[data-animate]');
  
    const observer = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            observer.unobserve(entry.target); // Optional: stop observing once visible
          }
        });
      },
      {
        threshold: 0.1, // Trigger when 10% of the container is visible
      }
    );
  
    containers.forEach(container => observer.observe(container));

    // Check for elements in the viewport on page load
    containers.forEach(container => {
        if (isInViewport(container)) {
            container.classList.add("visible");
        }
    });

    // Check for elements in the viewport on window resize
    window.addEventListener('resize', () => {
        containers.forEach(container => {
            if (isInViewport(container)) {
                container.classList.add("visible");
            }
        });
    });
});

// Function to check if an element is in the viewport
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

const contactForm = document.getElementById('contactForm');


if (contactForm) {
  contactForm.addEventListener('submit', function(event) {
  let isValid = true;

  // Full Name Validation (Min 3, Max 15 Characters)
  const name = document.getElementById('name');
  const nameError = document.getElementById('nameError');
  const nameValue = name.value.trim();
  if (nameValue === '') {
      nameError.textContent = "Name is required.";
      nameError.classList.remove('d-none');
      name.classList.add('is-invalid');
      isValid = false;
  } else if (nameValue.length < 3 || nameValue.length > 15) {
      nameError.textContent = "Name must be between 3 and 15 characters.";
      nameError.classList.remove('d-none');
      name.classList.add('is-invalid');
      isValid = false;
  } else {
      nameError.classList.add('d-none');
      name.classList.remove('is-invalid');
  }

   // Email Validation
   const email = document.getElementById('email');
   const emailError = document.getElementById('emailError');
   const emailValue = email.value.trim();
   const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
 
   if (emailValue === '') {
       emailError.textContent = "Email is required.";
       emailError.classList.remove('d-none');
       email.classList.add('is-invalid');
       isValid = false;
   } else if (!emailPattern.test(emailValue)) {
       emailError.textContent = "Please enter a valid email address.";
       emailError.classList.remove('d-none');
       email.classList.add('is-invalid');
       isValid = false;
   } else {
       emailError.classList.add('d-none');
       email.classList.remove('is-invalid');
   }
  

   // Phone Number Validation (Flexible International)
  const phone = document.getElementById('phone');
  const phoneError = document.getElementById('phoneError');
  const phoneValue = phone.value.trim();

  if (phoneValue === '') {
      phoneError.textContent = "Phone number is required.";
      phoneError.classList.remove('d-none');
      phone.classList.add('is-invalid');
      isValid = false;
  } else if (!/^\+?\d{7,15}$/.test(phoneValue)) {
      phoneError.textContent = "Please enter a valid phone number.";
      phoneError.classList.remove('d-none');
      phone.classList.add('is-invalid');
      isValid = false;
  } else {
      phoneError.classList.add('d-none');
      phone.classList.remove('is-invalid');
  }



  // Message Validation (Min 5 Characters)
  const message = document.getElementById('message');
  const messageError = document.getElementById('messageError');
  const messageValue = message.value.trim();
  if (messageValue === '') {
      messageError.textContent = "Message is required.";
      messageError.classList.remove('d-none');
      message.classList.add('is-invalid');
      isValid = false;
  } else if (messageValue.length < 5) {
      messageError.textContent = "Message must be at least 5 characters.";
      messageError.classList.remove('d-none');
      message.classList.add('is-invalid');
      isValid = false;
  } else {
      messageError.classList.add('d-none');
      message.classList.remove('is-invalid');
  }

  // Captcha Validation (only check empty, correctness = backend)
    const captchaInput = document.getElementById('captchaInput');
    const captchaError = document.getElementById('captchaError');
    const captchaValue = captchaInput.value.trim();

    if (captchaValue === '') {
      captchaError.textContent = "Captcha is required.";
      captchaError.classList.remove('d-none');
      captchaInput.classList.add('is-invalid');
      isValid = false;
    } else {
      captchaError.classList.add('d-none');
      captchaInput.classList.remove('is-invalid');
    }


  // Prevent form submission if invalid
  if (!isValid) {
      event.preventDefault();
  }
});
}




// Run animation when icons enter the viewport
document.addEventListener("DOMContentLoaded", () => {
  const elements = document.querySelectorAll(".roll");

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("active");
        observer.unobserve(entry.target); // only once
      }
    });
  }, { threshold: 0.2 });

  elements.forEach(el => observer.observe(el));
});




document.addEventListener("DOMContentLoaded", () => {
  const counters = document.querySelectorAll("[data-count]");
  let started = false; // run only once

  function startCounting() {
    counters.forEach(counter => {
      const target = +counter.getAttribute("data-count");
      let current = 0;

      // adjust divisor for slower animation (bigger divisor = slower)
      const increment = Math.max(1, Math.ceil(target / 1500)); 

      function updateCounter() {
        current += increment;

        if (current >= target) {
          counter.textContent = target + (target === 24 ? "/7" : "+");
        } else {
          counter.textContent = current;

          // use setTimeout for smoother slower animation
          setTimeout(updateCounter, 100); 
        }
      }

      updateCounter();
    });
  }

  const section = document.getElementById("why-choose");

  if (section) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !started) {
          startCounting();
          started = true;
          observer.disconnect();
        }
      });
    }, { threshold: 0.2 });

    observer.observe(section);

    // Extra check: if already in view on load
    const rect = section.getBoundingClientRect();
    if (rect.top < window.innerHeight && rect.bottom >= 0 && !started) {
      startCounting();
      started = true;
    }
  }
});
