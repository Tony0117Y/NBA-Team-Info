import { createRouter, createWebHistory } from "vue-router";
import TeamList from "../components/TeamList.vue";
import TeamInfo from "../components/TeamInfo.vue";

const routes = [
    {
      path: "/Teams", // Set /Teams as the path for the main page
      name: "TeamList",
      component: TeamList,
    },
    {
      path: "/teaminfo",
      name: "TeamInfo",
      component: TeamInfo,
    },
    {
      path: "/:pathMatch(.*)*", // Redirect unknown routes
      redirect: "/Teams",
    },
  ];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;