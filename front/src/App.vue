<script setup lang="ts">
import { client } from './api/client';
const handleImportFile = () => {
  client.post("/test", {
    name: "toto"
  })
}
</script>

<template>
  <article data-theme="dark">
    <label for="file">Import File</label>
    <input type="file" name="file" />
    <button @click="handleImportFile">Import</button>
  </article>
</template>

