<script lang="ts" setup>
import { onMounted, ref } from "vue";
import { getAccounts, addAccount } from "../api/account";
import { AccountDTO } from "../api/dtos/accountDTO";
const accounts = ref<AccountDTO[]>([]);

const account = ref<AccountDTO>({
  account_id: "",
  routing_number: "",
  branch_id: "",
});

onMounted(() => {
  getAccounts().then((data) => {
    accounts.value = data;
  });
});

const handleAddButton = () => {
  addAccount(account.value).then((data) => {
    accounts.value.push(data.__data__);
  });
};
</script>

<template>
  <figure>
    <div class="grid">
      <label for="account-id">
        Account ID
        <input
          v-model="account.account_id"
          type="text"
          name="account-id"
          placeholder="Account ID"
          required
        />
      </label>
      <label for="routing-number">
        Routing Number
        <input
          v-model="account.routing_number"
          type="text"
          name="routing-number"
          placeholder="Routing Number"
          required
        />
      </label>
      <label for="branch-id">
        Branch ID
        <input
          v-model="account.branch_id"
          type="text"
          name="branch-id"
          placeholder="Branch ID"
          required
        />
      </label>
    </div>
    <button @click="handleAddButton">Add</button>
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
