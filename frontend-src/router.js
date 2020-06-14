import Vue from 'vue';
import VueRouter from "vue-router";

import Home from "./view/Home";
import MapView from "./view/MapView";
import APIView from "./view/APIView";
Vue.use(VueRouter);

const routes = [
  { path: '/', component: Home, name: "Home" },
  { path: '/map', component: MapView, name: "MapView" },
  { path: '/api', component: APIView, name: "APIView" },
  // { path: '/dashboard', component: Dashboard, name: "Dashboard" },
  // { path: '/start/:game_id', component: Start, name: "Start" },
  // { path: '/results', component: Results, name: "Results" },
  // { path: '/failure/:game_id', component: Failure, name: "Failure" },
  // { path: '/success/:game_id', component: Success, name: "Success" },
  // { path: '/decode/:game_id', component: Decode, name: "Decode" },
  // { path: '/continue/:game_id', component: Continue, name: "Continue" },
  // { path: '/leaderboard', component: Leaderboard, name: "Leaderboard" },
  // { path: '/about', component: About, name: "About" },
  // { path: '/error', component: Error, name: "Error" },
];

const router = new VueRouter({
  routes
});

export default router;
