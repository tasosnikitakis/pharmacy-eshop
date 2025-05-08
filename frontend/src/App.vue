<script setup>
import { ref } from 'vue'; // Import ref for reactive data
import ProductList from './components/ProductList.vue';

// Placeholder data for featured categories
const featuredCategories = ref([
  { id: 1, name: 'Vitamins & Supplements', imageUrl: 'https://via.placeholder.com/300x200/A9DFBF/2E8B57?text=Vitamins', link: '#' },
  { id: 2, name: 'Skincare & Beauty', imageUrl: 'https://via.placeholder.com/300x200/FADBD8/C3278F?text=Skincare', link: '#' },
  { id: 3, name: 'Pain Relief', imageUrl: 'https://via.placeholder.com/300x200/AED6F1/2E86C1?text=Pain+Relief', link: '#' },
  { id: 4, name: 'First Aid', imageUrl: 'https://via.placeholder.com/300x200/F9E79F/B7950B?text=First+Aid', link: '#' }
]);

// Reactive ref for the search query
const searchQuery = ref('');

// Placeholder function for handling search submission
const handleSearch = () => {
  if (searchQuery.value.trim()) {
    alert(`Search initiated for: ${searchQuery.value}`); // Placeholder action
  } else {
    alert('Please enter a search term.'); // Placeholder action
  }
};


// Data for Promotional Blocks
const promoBlocks = ref([
  { id: 1, title: 'Free Delivery', text: 'On orders over €50' },
  { id: 2, title: 'Click & Collect', text: 'Pick up at your convenience' },
  { id: 3, title: 'Expert Advice', text: 'Our pharmacists are here to help' }
]);

// Data for Trust Signals
const trustSignals = ref([
  { id: 1, title: 'Qualified Pharmacists', text: 'Professional advice you can trust for your health needs.'},
  { id: 2, title: 'Genuine Products', text: 'We source only authentic products from reputable suppliers.' },
  { id: 3, title: 'Secure Shopping', text: 'Your data and payments are protected with top security.' }
]);

// Ref for newsletter email input
const newsletterEmail = ref('');

// Placeholder function for handling newsletter subscription
const handleSubscription = () => {
  if (newsletterEmail.value.trim() && newsletterEmail.value.includes('@')) { // Basic email check
    alert(`Subscribing with email: ${newsletterEmail.value}`);
    // Later, send this email to your backend or a mailing list service
    newsletterEmail.value = ''; // Clear the input after submission
  } else {
    alert('Please enter a valid email address.');
  }
};

</script>

<template>
  <div id="app-container">
    <header class="bg-light border-bottom mb-0 sticky-top shadow-sm">
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container">
          <a class="navbar-brand fw-bold" href="#">My Pharmacy E-Shop</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">All Products</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Categories</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Contact</a>
              </li>
            </ul>
            <form class="d-flex" role="search" @submit.prevent="handleSearch">
              <input 
                class="form-control me-2" 
                type="search" 
                placeholder="Search products..." 
                aria-label="Search"
                v-model="searchQuery"
                style="min-width: 220px;">
              <button class="btn btn-outline-primary" type="submit">Search</button>
            </form>
          </div>
        </div>
      </nav>
    </header>

    <section class="hero-section bg-primary text-white text-center py-5 mb-4 shadow-sm">
      <div class="container">
        <h1 class="display-4 fw-bold">Your Health, Our Priority</h1>
        <p class="lead my-3">Discover a wide range of healthcare products, vitamins, and wellness essentials. Delivered to your door.</p>
        <a href="#" class="btn btn-light btn-lg">Shop All Products</a>
      </div>
    </section>
    <section class="featured-categories py-4">
      <div class="container">
        <h2 class="text-center mb-4">Shop Our Top Categories</h2>
        <div class="row">
          <div v-for="category in featuredCategories" :key="category.id" class="col-6 col-md-3 mb-4 d-flex align-items-stretch">
            <div class="card w-100 text-center shadow-sm category-card">
              <a :href="category.link" class="text-decoration-none text-dark">
                <img :src="category.imageUrl" class="card-img-top category-image" :alt="category.name">
                <div class="card-body">
                  <h5 class="card-title category-name">{{ category.name }}</h5>
                </div>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="promotional-blocks py-4 bg-light">
      <div class="container">
        <div class="row text-center gy-3"> 
          <div v-for="promo in promoBlocks" :key="promo.id" class="col-lg-4 col-md-6 mb-3 mb-lg-0"> 
            <div class="p-3 promo-block-item">
              <h4 class="fw-semibold h5">{{ promo.title }}</h4>
              <p class="mb-0 text-muted small">{{ promo.text }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="trust-signals py-5">
      <div class="container">
        <h2 class="text-center mb-5">Why Choose Our Pharmacy?</h2>
        <div class="row text-center gy-4"> 
          <div v-for="signal in trustSignals" :key="signal.id" class="col-lg-4 col-md-6 mb-3 mb-lg-0"> 
            <div class="p-3 trust-signal-item">
              <h4 class="fw-semibold h5">{{ signal.title }}</h4>
              <p class="text-muted small">{{ signal.text }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <main class="container py-4">

      <h2 class="text-center mb-4">Browse Our Products</h2> 

      <ul class="nav nav-tabs justify-content-center mb-4" id="productTab" role="tablist">
        <li class="nav-item" role="presentation">
          <button 
            class="nav-link active" 
            id="featured-tab" 
            data-bs-toggle="tab" 
            data-bs-target="#featured-tab-pane" 
            type="button" 
            role="tab" 
            aria-controls="featured-tab-pane" 
            aria-selected="true">
            Featured
          </button>
        </li>
        <li class="nav-item" role="presentation">
          <button 
            class="nav-link" 
            id="new-arrivals-tab" 
            data-bs-toggle="tab" 
            data-bs-target="#new-arrivals-tab-pane" 
            type="button" 
            role="tab" 
            aria-controls="new-arrivals-tab-pane" 
            aria-selected="false">
            New Arrivals
          </button>
        </li>
        <li class="nav-item" role="presentation">
          <button 
            class="nav-link" 
            id="on-sale-tab" 
            data-bs-toggle="tab" 
            data-bs-target="#on-sale-tab-pane" 
            type="button" 
            role="tab" 
            aria-controls="on-sale-tab-pane" 
            aria-selected="false">
            On Sale
          </button>
        </li>
        <li class="nav-item" role="presentation">
          <button 
            class="nav-link" 
            id="all-products-tab" 
            data-bs-toggle="tab" 
            data-bs-target="#all-products-tab-pane" 
            type="button" 
            role="tab" 
            aria-controls="all-products-tab-pane" 
            aria-selected="false">
            All Products
          </button>
        </li>
      </ul>

      <div class="tab-content" id="productTabContent">
        <div class="tab-pane fade show active" id="featured-tab-pane" role="tabpanel" aria-labelledby="featured-tab" tabindex="0">
          <ProductList /> 
        </div>
        <div class="tab-pane fade" id="new-arrivals-tab-pane" role="tabpanel" aria-labelledby="new-arrivals-tab" tabindex="0">
          <p class="text-center py-5 text-muted">New arrivals coming soon!</p>
          </div>
        <div class="tab-pane fade" id="on-sale-tab-pane" role="tabpanel" aria-labelledby="on-sale-tab" tabindex="0">
          <p class="text-center py-5 text-muted">Sale products coming soon!</p>
          </div>
        <div class="tab-pane fade" id="all-products-tab-pane" role="tabpanel" aria-labelledby="all-products-tab" tabindex="0">
          <p class="text-center py-5 text-muted">All products list coming soon!</p>
          </div>
      </div>
    </main>

    <section class="newsletter-signup py-5 bg-secondary text-white">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-md-8 col-lg-6 text-center">
            <h2 class="mb-3">Stay Updated!</h2>
            <p class="mb-4">Subscribe to our newsletter for the latest deals, health tips, and new product updates.</p>
            <form class="d-flex" @submit.prevent="handleSubscription">
              <input 
                type="email" 
                class="form-control form-control-lg me-2" 
                placeholder="Enter your email address" 
                aria-label="Email Address"
                v-model="newsletterEmail"
                required>
              <button class="btn btn-primary btn-lg" type="submit">Subscribe</button>
            </form>
          </div>
        </div>
      </div>
    </section>

    <section class="brand-logos py-4 bg-light">
      <div class="container">
        <h4 class="text-center text-muted mb-4">Shop Popular Brands</h4>
        <div class="row align-items-center justify-content-center gy-3">
          <div class="col-6 col-sm-4 col-md-2 text-center">
            <img src="https://via.placeholder.com/150x60/dee2e6/6c757d?text=Brand+A" alt="Brand A Logo" class="img-fluid brand-logo">
          </div>
          <div class="col-6 col-sm-4 col-md-2 text-center">
            <img src="https://via.placeholder.com/150x60/dee2e6/6c757d?text=Brand+B" alt="Brand B Logo" class="img-fluid brand-logo">
          </div>
          <div class="col-6 col-sm-4 col-md-2 text-center">
            <img src="https://via.placeholder.com/150x60/dee2e6/6c757d?text=Brand+C" alt="Brand C Logo" class="img-fluid brand-logo">
          </div>
          <div class="col-6 col-sm-4 col-md-2 text-center">
            <img src="https://via.placeholder.com/150x60/dee2e6/6c757d?text=Brand+D" alt="Brand D Logo" class="img-fluid brand-logo">
          </div>
          <div class="col-6 col-sm-4 col-md-2 text-center">
            <img src="https://via.placeholder.com/150x60/dee2e6/6c757d?text=Brand+E" alt="Brand E Logo" class="img-fluid brand-logo">
          </div>
          <div class="col-6 col-sm-4 col-md-2 text-center">
            <img src="https://via.placeholder.com/150x60/dee2e6/6c757d?text=Brand+F" alt="Brand F Logo" class="img-fluid brand-logo">
          </div>
        </div>
      </div>
    </section>

    <footer class="footer mt-auto pt-5 pb-4 bg-dark text-white bg-opacity-75"> 
      <div class="container">
        <div class="row gy-4"> 

          
          <div class="col-lg-4 col-md-6">
            <h5 class="mb-3">My Pharmacy E-Shop</h5>
            <p class="small text-muted">Your trusted partner for health and wellness products. Providing quality care and expert advice.</p>
          </div>

          
          <div class="col-lg-2 col-md-3 col-6">
            <h5 class="mb-3">Links</h5>
            <ul class="list-unstyled small">
              <li class="mb-2"><a href="#" class="text-white text-decoration-none link-hover">About Us</a></li>
              <li class="mb-2"><a href="#" class="text-white text-decoration-none link-hover">Contact Us</a></li>
              <li class="mb-2"><a href="#" class="text-white text-decoration-none link-hover">All Products</a></li>
              <li class="mb-2"><a href="#" class="text-white text-decoration-none link-hover">Categories</a></li>
            </ul>
          </div>

          <div class="col-lg-2 col-md-3 col-6">
            <h5 class="mb-3">Support</h5>
            <ul class="list-unstyled small">
              <li class="mb-2"><a href="#" class="text-white text-decoration-none link-hover">FAQ</a></li>
              <li class="mb-2"><a href="#" class="text-white text-decoration-none link-hover">Shipping Info</a></li>
              <li class="mb-2"><a href="#" class="text-white text-decoration-none link-hover">Returns Policy</a></li>
            </ul>
          </div>

          <div class="col-lg-4 col-md-12 text-lg-end"> 
            <h5 class="mb-3">Connect With Us</h5>
            <p class="small text-muted mb-2"> Placeholder for social icons </p>
            <ul class="list-unstyled small mt-3">
              <li class="mb-2"><a href="#" class="text-white text-decoration-none link-hover">Privacy Policy</a></li>
              <li class="mb-2"><a href="#" class="text-white text-decoration-none link-hover">Terms & Conditions</a></li>
            </ul>
          </div>

        </div>
        <hr class="my-4"> 
        <div class="row">
          <div class="col text-center small text-muted">
            &copy; {{ new Date().getFullYear() }} My Pharmacy E-Shop. All rights reserved.
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<style scoped>
#app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.category-card {
  transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
}

.category-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15) !important;
}

.category-image {
  height: 150px;
  object-fit: cover;
  border-bottom: 1px solid #eee;
}

.category-name {
  font-size: 1.1rem;
  font-weight: 500;
}

.promo-block-item h4, .trust-signal-item h4 {
  color: var(--bs-primary); /* Example: Use Bootstrap primary color */
}

main {
  flex-grow: 1; 
}

.brand-logo {
  max-height: 45px; /* Control the max height */
  filter: grayscale(100%); /* Make them grayscale initially */
  opacity: 0.6;
  transition: all 0.3s ease-in-out;
}

.brand-logo:hover {
  filter: grayscale(0%); /* Color on hover */
  opacity: 1;
  transform: scale(1.1);
}

.footer a.link-hover:hover {
  text-decoration: underline !important; /* Ensure underline appears */
  opacity: 0.8;
}

.footer hr {
   border-top: 1px solid rgba(255, 255, 255, 0.2); /* Lighter hr for dark background */
}

</style>