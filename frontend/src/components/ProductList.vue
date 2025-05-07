<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const products = ref([]);
const isLoading = ref(true);
const error = ref(null);

const fetchProducts = async () => {
  console.log('fetchProducts function CALLED'); // <--- Add/Verify
  isLoading.value = true;
  error.value = null;
  try {
    // Make sure your Django development server is running on port 8000
    const response = await axios.get('http://127.0.0.1:8000/api/products/');
    console.log('API Response:', response.data); // <--- Add/Verify
    products.value = response.data;
    console.log('products.value SET TO:', products.value); // <--- Add/Verify
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
onMounted(fetchProducts);
console.log('ProductList component MOUNTED'); // <--- Add/Verify
</script>

<template>
  <div class="product-list-container">
    <h1>Our Products</h1>

    <div v-if="isLoading" class="loading">Loading products...</div>

    <div v-if="error" class="error-message">
      <p>Could not load products. Please try again later.</p>
      <p>Details: {{ error }}</p>
      <button @click="fetchProducts">Retry</button>
    </div>

    <div v-if="!isLoading && !error && products.length === 0" class="no-products">
      No products found.
    </div>

    <div v-if="!isLoading && !error && products.length > 0" class="products-grid">
      <div v-for="product in products" :key="product.id" class="product-card">
        <img v-if="product.image" :src="product.image" :alt="product.name" class="product-image" />
        <img v-else src="https://via.placeholder.com/150?text=No+Image" alt="No image available" class="product-image">
        <h2>{{ product.name }}</h2>
        <p class="description">{{ product.description }}</p>
        <p class="price">Price: €{{ product.price }}</p>
        <p v-if="product.category">Category: {{ product.category }}</p>
        <p v-if="product.brand">Brand: {{ product.brand }}</p>
        <p v-if="product.stock">Stock: {{ product.stock }}</p>
        <div v-if="product.discount_price && product.discount_price !== product.original_price">
          <p class="original-price">Original: €{{ product.original_price }}</p>
          <p class="discount-price">Now: €{{ product.discount_price }} ({{ product.discount_rate }}% off)</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.product-list-container {
  font-family: Arial, sans-serif;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.loading,
.error-message,
.no-products {
  text-align: center;
  padding: 20px;
  font-size: 1.2em;
}

.error-message {
  color: red;
  border: 1px solid red;
  background-color: #ffebeb;
  border-radius: 5px;
}

.error-message button {
  margin-top: 10px;
  padding: 8px 15px;
  cursor: pointer;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
}

.product-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  text-align: center;
  box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
}

.product-image {
  max-width: 100%;
  height: 150px; /* Fixed height for consistency */
  object-fit: contain; /* Changed from 'cover' to 'contain' to show whole image */
  margin-bottom: 15px;
  border-radius: 4px;
}

.product-card h2 {
  font-size: 1.3em;
  margin: 10px 0;
}

.product-card .description {
  font-size: 0.9em;
  color: #555;
  min-height: 50px; /* Give some space for description */
}

.product-card .price {
  font-size: 1.1em;
  font-weight: bold;
  color: #333;
  margin-top: 10px;
}

.original-price {
    text-decoration: line-through;
    color: #999;
    font-size: 0.9em;
}
.discount-price {
    color: #d9534f; /* A reddish color for discount */
    font-weight: bold;
}
</style>