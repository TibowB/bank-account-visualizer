<script setup lang="ts">
import { ref } from "vue";
import { importFile } from "../api/import";
const fileInput = ref<HTMLInputElement>();
const account = ref<string>("");
const statement = ref<string>("");

const handleImportFile = async () => {
  if (fileInput.value === undefined || fileInput.value.files === null) {
    return;
  }

  const file = fileInput.value.files[0];

  importFile(file).then((data) => {
    account.value = `Account : ${data.account.account_id} ${data.account.routing_number} ${data.account.branch_id}`;
    statement.value = `Statement : ${data.statement.start_date} ${data.statement.end_date} ${data.statement.balance}`;
  });
};
</script>

<template>
  <article>
    <label for="file">Import File</label>
    <input ref="fileInput" type="file" name="file" />
    <button @click="handleImportFile">Import</button>
    <p>{{ account }}</p>
    <p>{{ statement }}</p>
  </article>
</template>
