<script lang="ts">
import axios from "axios";
import Navbar from "./Navbar.vue";

export default {
  data: () => ({
    title: "",
    genre: "",
    genres: [],
    songFile: undefined,
    imageFile: undefined,
    image: "",
    lyrics: "",
    is_private: false,
    showError: false,
  }),
  components: { Navbar },
  async mounted() {
    // get song genres for v-select
    await axios
      .get("backend/genre/", {
        headers: {
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      })
      .then((response) => {
        // need genre id for post request, in this format is easy with v-select
        this.genres = Object.values(response["data"]).map((genre) => ({
          value: genre.id,
          title: genre.name,
        }));
      });
  },
  methods: {
    async submit() {
      try {
        let formData = new FormData();
        formData.append("user_id", localStorage.getItem("user_id"));
        formData.append("title", this.title);
        formData.append("song_path", this.songFile[0], this.songFile[0].name);
        formData.append(
          "song_cover ",
          this.imageFile[0],
          this.imageFile[0].name
        );
        formData.append("lyrics", this.lyrics);
        formData.append("is_private", this.is_private);
        formData.append("genre", this.genre.value);

        await axios
          .post("backend/song/", formData, {
            headers: {
              "Content-Type": "multipart/form-data",
              Authorization: `Token ${localStorage.getItem("token")}`,
            },
          })
          .then((response) => {
            this.$router.push({ name: "home" });
          })
          .catch((error) => {
            // show error message
            this.showError = true;
            console.log(error);
          });
      } catch (error) {
        // show error
        this.showError = true;
      }
    },
  },
};
</script>

<template>
  <v-app class="song-page">
    <Navbar> </Navbar>

    <v-main class="add-song-content">
      <div class="mx-auto mt-5">
        <v-icon icon="mdi-music" size="52"></v-icon>
      </div>
      <h1>Add a music</h1>

      <div class="add-song-form">
        <v-divider class="mt-2"></v-divider>

        <v-form>
          <v-text-field
            v-model="title"
            class="mt-5"
            label="Music title"
            outlined
            clearable
          ></v-text-field>

          <v-file-input
            v-model="songFile"
            class="mt-3"
            label="Audio file"
            accept="audio/*"
          ></v-file-input>

          <v-file-input
            v-model="imageFile"
            class="mt-3"
            label="Cover"
            accept="image/*"
          ></v-file-input>

          <v-select
            v-model="genre"
            :items="genres"
            class="mt-3"
            label="Genre"
            outlined
            clearable
            return-object
          >
          </v-select>

          <v-textarea
            v-model="lyrics"
            class="mt-3"
            label="Lyrics..."
            outlined
            clearable
          >
          </v-textarea>

          <v-checkbox v-model="is_private" label="Private"></v-checkbox>

          <v-divider></v-divider>

          <v-btn @click="submit" class="mt-5 mb-5"> Add music </v-btn>
        </v-form>

        <v-snackbar v-model="showError" :timeout="1000">
          <v-icon color="red">mdi-alert-circle</v-icon>
          <span color="red">Something went wrong! Retry please</span>
          <v-icon @click="showError = false">mdi-close</v-icon>
        </v-snackbar>
      </div>
    </v-main>
  </v-app>
</template>

<style scoped>
.add-song-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: auto;
  text-align: center;
  width: 30%;
  min-width: 200px;
}
</style>
