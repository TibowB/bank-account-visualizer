import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router";
import Account from "../views/Account.vue";
import Home from "../views/Home.vue";
import Import from "../views/Import.vue";
const routes: RouteRecordRaw[] = [
  { path: "/", component: Home },
  { path: "/account", component: Account },
  { path: "/import", component: Import },
];

export const router = createRouter({
  history: createWebHashHistory(),
  routes,
});
