<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const products = ref([]);
const isLoading = ref(true);
const error = ref(null);

const fetchProducts = async () => {
  console.log('fetchProducts function CALLED');
  isLoading.value = true;
  error.value = null;
  try {
    // Make sure your Django development server is running on port 8000
    const response = await axios.get('http://127.0.0.1:8000/api/products/');
    console.log('API Response:', response.data);
    products.value = response.data;
    console.log('products.value SET TO:', products.value);
  } catch (e) {
    console.error('Failed to fetch products:', e);
    if (e.response) {
      // Server responded with a status code out of 2xx range
      error.value = `Error ${e.response.status}: ${e.response.data.detail || e.message}`;
    } else if (e.request) {
      // Request was made but no response was received
      error.value = 'No response from server. Is the backend running?';
    } else {
      // Something happened in setting up the request
      error.value = `Failed to fetch products: ${e.message}`;
    }
  } finally {
    isLoading.value = false;
  }
};

// Fetch products when the component is mounted
onMounted(() => {
  console.log('ProductList component MOUNTED');
  fetchProducts();
});
</script>

<template>
  <div class="product-list-container py-4"> <h1 class="mb-4 text-center">Our Products</h1> <div v-if="isLoading" class="loading text-center">
      <div class="spinner-border text-primary" role="status" style="width: 3rem; height: 3rem;">
        <span class="visually-hidden">Loading...</span>
      </div>
      <p class="mt-2">Loading products...</p>
    </div>

    <div v-if="error" class="error-message alert alert-danger">
      <p class="fw-bold">Could not load products.</p>
      <p>Details: {{ error }}</p>
      <button @click="fetchProducts" class="btn btn-danger mt-2">Retry</button>
    </div>

    <div v-if="!isLoading && !error && products.length === 0" class="no-products text-center py-5">
      <p class="lead">No products found at the moment.</p>
      </div>

    <div v-if="!isLoading && !error && products.length > 0" class="row">
      <div v-for="product in products" :key="product.id" class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4 d-flex align-items-stretch">
        <div class="card h-100 shadow-sm w-100"> <img 
            v-if="product.image" 
            :src="product.image" 
            :alt="product.name" 
            class="card-img-top" 
            style="height: 200px; object-fit: contain; padding: 10px;" />
          <img 
            v-else 
            src="https://via.placeholder.com/300x200?text=No+Image" 
            alt="No image available" 
            class="card-img-top"
            style="height: 200px; object-fit: cover; padding: 10px;" />

          <div class="card-body d-flex flex-column"> <h5 class="card-title">{{ product.name }}</h5>
            <p class="card-text text-muted small flex-grow-1 description-text">
              {{ product.description ? (product.description.length > 100 ? product.description.substring(0, 100) + '...' : product.description) : 'No description available.' }}
            </p>
            
            <div class="mt-2"> <p class="card-text h5 mb-0 text-primary fw-bold">€{{ parseFloat(product.price).toFixed(2) }}</p>
              <div v-if="product.discount_price && parseFloat(product.discount_price) < parseFloat(product.price)">
                 <small class="text-muted text-decoration-line-through">Original: €{{ parseFloat(product.original_price || product.price).toFixed(2) }}</small>
                 <p class="card-text h5 text-danger fw-bold">Now: €{{ parseFloat(product.discount_price).toFixed(2) }} 
                   <span v-if="product.discount_rate" class="badge bg-danger ms-1">{{ product.discount_rate }}% off</span>
                 </p>
              </div>
            </div>

            <p v-if="product.category" class="card-text mt-2 mb-0"><small class="text-muted">Category: {{ product.category }}</small></p>
            <p v-if="product.brand" class="card-text mb-2"><small class="text-muted">Brand: {{ product.brand }}</small></p>

            <div class="mt-auto pt-2"> <a href="#" class="btn btn-primary w-100 mb-1">View Details</a>
              </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Minimal scoped styles, as Bootstrap handles most of it */

.card-img-top {
  border-bottom: 1px solid #eee; /* Adds a subtle line below the image */
}

.description-text {
  min-height: 60px; /* Ensures a minimum height for description area, helps card alignment if descriptions vary a lot */
}

/* If you want to ensure all cards in a row truly have the same height, 
   the `d-flex align-items-stretch` on the column (`.col-*`) and `h-100` on the card is a good combination.
   However, `h-100` on the card works when the parent column is also part of a flex row.
   The `align-items-stretch` on the column is key if the row itself is display:flex (which Bootstrap rows are).
*/
</style>