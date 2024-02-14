<script lang="ts">
import axios from "axios";

export default {
  data: () => ({
    drawer: false,
    username: "",
    image: "",
  }),
  methods: {
    home() {
      this.$router.push({ name: "home" });
    },
    addSong() {
      this.$router.push({ name: "add_song" });
    },
    disconnect() {
      localStorage.clear();
      this.$router.push({ name: "index" });
    },
    account() {
      this.$router.push({ name: "account" });
    },
  },
  async mounted() {
    await axios
      .get(`backend/users/${localStorage.getItem("user_id")}`, {
        headers: {
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      })
      .then((response) => {
        this.username = response["data"]["username"];
        this.image = response["data"]["profile_picture"];
      });
  },
};
</script>

<template>
  <v-navigation-drawer v-model="drawer">
    <v-sheet class="pa-4">
      <v-avatar class="mb-2" size="96">
        <img :src="image" alt="Profile picture" height="96" />
      </v-avatar>

      <div>{{ username }}</div>
    </v-sheet>

    <v-divider></v-divider>

    <v-container class="nav-bar-btn">
      <v-btn
        @click="account"
        color="green"
        prepend-icon="mdi-account"
        class="btn-nav mb-2"
        >My Account</v-btn
      >
      <v-btn
        @click="addSong"
        color="primary"
        prepend-icon="mdi-music"
        class="btn-nav mb-2"
        >Add Song</v-btn
      >
      <v-btn
        @click="disconnect"
        color="red"
        prepend-icon="mdi-account-remove"
        class="btn-nav mb-2"
        >Disconnect</v-btn
      >
    </v-container>
  </v-navigation-drawer>

  <v-app-bar>
    <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
    <div class="nav-bar-title" @click="home">
      <div class="nav-bar-index-logo-img"></div>
      <v-toolbar-title>PineAppleMusic</v-toolbar-title>
    </div>
  </v-app-bar>
</template>

<style scoped>
.pa-4 {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.nav-bar-title {
  display: flex;
  flex-direction: row;
  align-items: center;
  cursor: pointer;
}

.nav-bar-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 200px;
}

.btn-nav {
  width: 200px;
}
</style>
