<script lang="ts" setup>
import { onMounted, ref } from "vue";
import { getAccounts } from "../api/account";
import { AccountDTO } from "../api/dtos/accountDTO";
const accounts = ref<AccountDTO[]>([]);

onMounted(() => {
  getAccounts().then((data) => {
    accounts.value = data;
  });
});
</script>

<template>
  <figure>
    <table>
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Account ID</th>
          <th scope="col">Routing Number</th>
          <th scope="col">Branch ID</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(account, index) of accounts">
          <th scope="row">{{ index + 1 }}</th>
          <td>{{ account.account_id }}</td>
          <td>{{ account.routing_number }}</td>
          <td>{{ account.branch_id }}</td>
        </tr>
      </tbody>
    </table>
  </figure>
</template>
