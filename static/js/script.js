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
