<script lang="ts" setup>
import NavBar from "./components/NavBar.vue";
import Account from "./views/Account.vue";
import Import from "./views/Import.vue";
</script>

<template>
  <NavBar />
  <main class="container">
    <Account />
    <Import />
  </main>
</template>
