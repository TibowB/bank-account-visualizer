<script setup lang="ts">
import { ref } from "vue";
import { importFile } from "../api/import";
const fileInput = ref<HTMLInputElement>();
const message = ref<string>("");
const isLoading = ref<boolean>(false);

const handleImportFile = async () => {
  if (fileInput.value === undefined || fileInput.value.files === null) {
    return;
  }

  isLoading.value = true;

  const file = fileInput.value.files[0];

  importFile(file)
    .then((data) => {
      message.value = data;
      setTimeout(() => (message.value = ""), 3000);
    })
    .finally(() => {
      isLoading.value = false;
    });
};
</script>

<template>
  <article>
    <label for="file">Import File</label>
    <input ref="fileInput" type="file" name="file" />
    <button @click="handleImportFile" :aria-busy="isLoading">Import</button>
    <p>{{ message }}</p>
  </article>
</template>
