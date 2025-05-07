<script setup>
// This line imports your ProductList component
import ProductList from './components/ProductList.vue';
</script>

<template>
  <div id="app-container">
    <header>
      <h1>My Pharmacy E-Shop</h1>
    </header>
    <main>
      <ProductList /> </main>
    <footer>
      <p>&copy; {{ new Date().getFullYear() }} My Pharmacy E-Shop. All rights reserved.</p>
    </footer>
  </div>
</template>

<style scoped>
#app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  text-align: center; /* Center align text for header/footer */
}

header {
  background-color: #42b983; /* A Vue-green like color */
  color: white;
  padding: 20px 0;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

header h1 {
  margin: 0;
  font-size: 2em;
}

main {
  flex-grow: 1; /* Allows main content to take up available space */
  padding: 20px;
}

footer {
  background-color: #333;
  color: #fff;
  padding: 15px 0;
  margin-top: auto; /* Pushes footer to the bottom */
  font-size: 0.9em;
}

/* Remove any default global styles from Vite if they were targeting elements removed */
/* For example, if there were styles for #app centering elements directly,
   and we removed those elements, those styles might not be needed or could be adjusted.
   The styles below are just basic styling for the new App.vue structure.
*/
</style>