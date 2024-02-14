<script lang="ts">
export default {
  data() {
    return {};
  },
  methods: {},
};
</script>

<template>
  <v-app class="index-page">
    <v-main class="index-content">
      <v-container class="index-logo-img"></v-container>

      <v-container class="index-text">
        <h1>Enjoy your music</h1>
      </v-container>

      <v-container class="index-btn">
        <v-btn
          :to="{ name: 'login' }"
          variant="outlined"
          color="white"
          class="login-btn"
        >
          Connect
        </v-btn>

        <v-btn
          :to="{ name: 'signup' }"
          variant="outlined"
          color="white"
          class="signup-btn"
        >
          Sign up
        </v-btn>
      </v-container>
    </v-main>
  </v-app>
</template>

<style scoped></style>
