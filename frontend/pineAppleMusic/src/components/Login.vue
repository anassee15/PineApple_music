<script lang="ts">
import axios from "axios";

export default {
  data: () => ({
    visible: false,
    username: "",
    password: "",
    alert: false,
  }),
  methods: {
    async login() {
      await axios
        .post("/auth/login/", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          // get token from response
          localStorage.setItem("token", response["data"]["token"]);

          axios
            .get(`backend/users?username=${this.username}`, {
              headers: {
                Authorization: `Token ${response["data"]["token"]}`,
              },
            })
            .then((response) => {
              localStorage.setItem("user_id", response["data"][0]["id"]);

              // redirect to home page
              this.$router.push({ name: "home" });
            });
        })
        .catch((error) => {
          // show error message
          console.log(error);
          this.alert = true;
        });
    },
  },
};
</script>

<template>
  <v-app class="login-page">
    <v-main class="login-content">
      <v-container class="login-logo">
        <div class="login-logo-img"></div>
        <div class="login-text">
          <h1>pineAppleMusic</h1>
        </div>
      </v-container>

      <v-divider mode="presentation" color="white"></v-divider>

      <h3 id="login-text">To continue, log in.</h3>

      <div>
        <v-alert
          v-model="alert"
          type="warning"
          color="red"
          variant="tonal"
          class="login-alert"
          >Username or Password incorrect.</v-alert
        >
      </div>

      <v-form class="login-form">
        <v-text-field
          v-model="username"
          label="Username"
          outlined
          dense
          clearable
          color="purple"
        ></v-text-field>

        <v-text-field
          v-model="password"
          label="Password"
          outlined
          dense
          clearable
          color="purple"
          :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
          :type="visible ? 'text' : 'password'"
          @click:append-inner="visible = !visible"
        ></v-text-field>

        <v-btn @click="login" color="success" class="login-btn"> Log in </v-btn>
      </v-form>

      <v-divider mode="presentation" color="white"></v-divider>

      <v-container class="no-account-login">
        <p>
          Don't have an account ?
          <router-link :to="{ name: 'signup' }">Sign up</router-link>
        </p>
      </v-container>
    </v-main>
  </v-app>
</template>

<style scoped></style>
