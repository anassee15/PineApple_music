import { createRouter, createWebHistory } from "vue-router";

import Index from "./components/Index.vue";
import Login from "./components/Login.vue";
import Signup from "./components/Signup.vue";
import Home from "./components/Home.vue";
import Account from "./components/MyAccount.vue";
import AddSong from "./components/AddSong.vue";
import Song from "./components/Song.vue";
import Profile from "./components/Profile.vue";

const routes = [
  { path: "/", name: "", component: Index },
  { path: "/index", name: "index", component: Index },
  { path: "/login", name: "login", component: Login },
  { path: "/signup", name: "signup", component: Signup },
  { path: "/home", name: "home", component: Home },
  { path: "/account", name: "account", component: Account },
  { path: "/add_song", name: "add_song", component: AddSong},
  { path: "/song/:id", name: "song", component: Song, props: true},
  { path: "/profile/:id", name: "profile", component: Profile, props: true},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// // control access to routes
router.beforeEach((to, from, next) => {
  const publicPages = ["/", "/index", "/login", "/signup"];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem('token');
  
  if (authRequired && !loggedIn) {
    return next("/");
  }
  
  next();
});

export { router };
