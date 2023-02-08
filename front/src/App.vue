<script setup lang="ts">
import { ref } from "vue";
import { importFile } from "./api/import";
const fileInput = ref<HTMLInputElement>();

const handleImportFile = async () => {
  if (fileInput.value === undefined || fileInput.value.files === null) {
    return;
  }

  const file = fileInput.value.files[0];

  await importFile(file);
};
</script>

<template>
  <article data-theme="dark">
    <label for="file">Import File</label>
    <input ref="fileInput" type="file" name="file" />
    <button @click="handleImportFile">Import</button>
  </article>
</template>
