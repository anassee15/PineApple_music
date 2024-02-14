<script lang="ts">
import axios from "axios";

export default {
  data: () => ({
    email: "",
    username: "",
    password: "",
    password2: "",
    gender: "",
    is_artist: false,
    visible: false,
    items: ["Man", "Woman", "Other"],
    profile_picture: undefined,
    description: "",
    rules: {
      required: (value: any) => !!value || "Required.",
      min: (value: string | any[]) => value.length >= 8 || "Min 8 characters",
      minUsername: (value: string | any[]) =>
        value.length >= 3 || "Min 3 characters",
      minDesc: (value: string | any[]) =>
        value.length >= 15 || "Min 15 characters",
      email: (value: string) => {
        const pattern =
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return pattern.test(value) || "Invalid e-mail.";
      },
      password: (value: string) => {
        const pattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;
        return (
          pattern.test(value) || "need 8 characters, one uppercase, one number."
        );
      },
    },
  }),
  methods: {
    async register() {
      let form_data = new FormData();

      form_data.append("email", this.email);
      form_data.append("username", this.username);
      form_data.append("password", this.password);
      form_data.append("password2", this.password2);
      form_data.append("gender", this.gender.toUpperCase());
      form_data.append("is_artist", this.is_artist);
      form_data.append(
        "profile_picture",
        this.profile_picture[0],
        this.profile_picture[0].name
      );
      form_data.append("description", this.description);

      await axios
        .post("/backend/user/register", form_data, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          // get token from response
          axios.defaults.headers.common["Authorization"] =
            response["data"]["token"];

          // redirect to home page
          this.$router.push({ name: "home" });
        })
        .catch((error) => {
          // show error message
          console.log(error);
        });
    },
    matchingPasswords: function () {
      if (this.password2.length === this.password.length) {
        return this.password2 === this.password || "Passwords does not match.";
      } else if (
        this.password.slice(0, this.password2.length) === this.password2
      ) {
        return true;
      } else {
        return "Passwords does not match.";
      }
    },
  },
};
</script>

<template>
  <v-app class="signup-page">
    <v-main class="signup-content">
      <v-container class="signup-logo">
        <div class="signup-logo-img"></div>
        <div class="signup-text">
          <h1>pineAppleMusic</h1>
        </div>
      </v-container>

      <v-divider mode="presentation" color="white"></v-divider>

      <h3 id="signup-text">Create an account.</h3>

      <v-form class="signup-form">
        <v-text-field
          v-model="email"
          label="Email"
          outlined
          dense
          clearable
          hint="enter your email address"
          :rules="[rules.required, rules.email]"
          color="purple"
        ></v-text-field>

        <v-text-field
          v-model="username"
          label="Username"
          outlined
          dense
          clearable
          hint="How should we call you ?"
          color="purple"
          :rules="[rules.required, rules.minUsername]"
        ></v-text-field>

        <v-text-field
          v-model="password"
          label="Password"
          outlined
          dense
          clearable
          hint="Enter your password"
          color="purple"
          :rules="[rules.required, rules.min, rules.password]"
          :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
          :type="visible ? 'text' : 'password'"
          @click:append-inner="visible = !visible"
        ></v-text-field>

        <v-text-field
          v-model="password2"
          label="Confirm password"
          outlined
          dense
          clearable
          hint="Enter your password again"
          :type="'password'"
          :rules="[rules.required, matchingPasswords]"
          color="purple"
        ></v-text-field>

        <v-select
          v-model="gender"
          :items="items"
          label="What is your gender ?"
          color="purple"
          :rules="[rules.required]"
        ></v-select>

        <v-textarea
          v-model="description"
          label="Description"
          outlined
          dense
          color="purple"
          hint="Tell us about yourself..."
          :rules="[rules.required, rules.minDesc]"
        >
        </v-textarea>

        <v-file-input
          v-model="profile_picture"
          show-size
          accept="image/*"
          label="Profile picture"
          color="purple"
          :rules="[rules.required]"
        ></v-file-input>

        <v-checkbox
          v-model="is_artist"
          :label="'I am an artist.'"
          class="artist-checkbox"
        ></v-checkbox>

        <v-btn @click="register" color="success" class="signup-btn">
          Confirm
        </v-btn>
      </v-form>

      <v-divider mode="presentation" color="white"></v-divider>

      <v-container class="have-account-signup">
        <p>
          Already have an account ?
          <router-link :to="{ name: 'login' }">Log in</router-link>
        </p>
      </v-container>
    </v-main>
  </v-app>
</template>

<style scoped>
.artist-checkbox {
  display: flex;
  justify-content: center;
  margin-bottom: 0.5em;
}
</style>
