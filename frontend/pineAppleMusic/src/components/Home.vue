<script lang="ts">
import axios from "axios";
import Navbar from "./Navbar.vue";
import Chart from "chart.js/auto";

export default {
  data: () => ({
    search: "",
    currentCase: "",
    songs: [],
    all_songs: "",
    all_users: "",
    filteredSongs: [],
    filteredUsers: [],
    genres: [],
  }),

  components: { Navbar },
  methods: {
    async searchUsersAndMusics() {
      // search songs
      this.filteredSongs = this.all_songs.filter((song) => {
        return song.title.toLowerCase().includes(this.search.toLowerCase());
      });

      // search users
      this.filteredUsers = this.all_users.filter((user) => {
        return user.username.toLowerCase().includes(this.search.toLowerCase());
      });
    },
    toSong(id: number) {
      // go to song page
      this.$router.push({ name: "song", params: { id: id } });
    },
    toUser(id: number) {
      // go to user page, if user is current user, go to account page
      if (id == localStorage.getItem("user_id")) {
        this.$router.push({ name: "account" });
      } else {
        this.$router.push({ name: "profile", params: { id: id } });
      }
    },
    createChart() {
      const ctx = document.getElementById("myChart") as HTMLCanvasElement;

      // get genre popularity data from songs and genres by nb_likes
      let genrePopularity: {
        [key: number]: { name: string; likes: number };
      } = {};

      for (const genre of this.genres) {
        genrePopularity[genre.id] = { name: genre.name, likes: 0 };
      }

      for (const song of this.all_songs) {
        if (song.genre.length > 0) {
          genrePopularity[song.genre[0]].likes += song.nb_likes;
        }
      }

      // sort by likes
      const sortedGenres = Object.values(genrePopularity).sort(
        (a, b) => b.likes - a.likes
      );

      // top 5 genres
      sortedGenres.splice(5);
      const labels = sortedGenres.map((genre) => genre.name);
      const data = sortedGenres.map((genre) => genre.likes);

      // create chart
      const myChart = new Chart(ctx, {
        type: "bar",
        data: {
          labels: labels,
          datasets: [
            {
              label: "# of Likes",
              data: data,
              backgroundColor: [
                "rgba(255, 99, 132, 0.2)",
                "rgba(54, 162, 235, 0.2)",
                "rgba(255, 206, 86, 0.2)",
                "rgba(75, 192, 192, 0.2)",
                "rgba(153, 102, 255, 0.2)",
              ],
              borderColor: [
                "rgba(255, 99, 132, 1)",
                "rgba(54, 162, 235, 1)",
                "rgba(255, 206, 86, 1)",
                "rgba(75, 192, 192, 1)",
                "rgba(153, 102, 255, 1)",
              ],
              borderWidth: 1,
            },
          ],
        },
        options: {
          animation: {
            duration: 2000,
            easing: "easeOutQuart",
          },
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      });
    },
  },
  async mounted() {
    // get songs
    await axios
      .get("backend/song", {
        headers: {
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      })
      .then((response) => {
        let i = 1;
        // get all songs for search
        this.all_songs = response["data"];

        // get 15 latest songs
        while (i < 15 && i < response["data"].length + 1) {
          this.songs.push(response["data"].slice(-i)[0]);
          i++;
        }
      });

    // get all users for search
    await axios
      .get("backend/users", {
        headers: {
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      })
      .then((response) => {
        this.all_users = response["data"];
      });

    // get genres for chart
    await axios
      .get("backend/genre/", {
        headers: {
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      })
      .then((response) => {
        this.genres = Object.values(response["data"]);
      });

    // create chart
    this.createChart();
  },
};
</script>

<template>
  <v-app class="home-page">
    <Navbar> </Navbar>

    <v-main class="home-content">
      <v-container class="mx-auto">
        <v-text-field
          v-model="search"
          @keyup="searchUsersAndMusics"
          prepend-inner-icon="mdi-magnify"
          label="Search music or user..."
          outlined
          clearable
        >
        </v-text-field>
      </v-container>

      <div v-if="search">
        <div v-if="filteredUsers.length == 0 && filteredSongs.length == 0">
          <v-container>
            <p>No results...</p>
          </v-container>
        </div>
        <div v-if="filteredUsers.length > 0">
          <v-container>
            <h3>Users</h3>
          </v-container>

          <v-container>
            <v-row>
              <v-col
                v-for="(user, index) of filteredUsers"
                :key="index"
                cols="6"
                md="2"
                class="col-centered"
              >
                <v-sheet @click="toUser(user['id'])" class="profile_picture">
                  <img :src="user['profile_picture']" alt="Profile picture" />
                </v-sheet>
                <span class="username">{{ user["username"] }}</span>
              </v-col>
            </v-row>
          </v-container>
        </div>
        <div v-if="filteredSongs.length > 0">
          <v-container>
            <h3>Musics</h3>
          </v-container>

          <v-container>
            <v-row>
              <v-col
                v-for="(song, index) of filteredSongs"
                :key="index"
                cols="6"
                md="2"
                class="col-centered"
              >
                <v-sheet
                  @click="toSong(song['id'])"
                  class="song-cover"
                  @mouseover="currentCase = `${index}`"
                  @mouseleave="currentCase = ''"
                >
                  <!-- Box content that is only displayed when the mouse is over it -->
                  <div v-if="currentCase === `${index}`" class="like-comment">
                    {{ song["nb_likes"] }}
                    <v-icon
                      icon="mdi-heart-outline"
                      class="mr-3"
                      small
                    ></v-icon>
                    {{ song["nb_comments"] }}
                    <v-icon icon="mdi-comment-text-outline" small></v-icon>
                  </div>

                  <img
                    :src="song['song_cover']"
                    alt="Profile picture"
                    :style="
                      currentCase === `${index}`
                        ? 'opacity: 0.4;'
                        : 'opacity: 1;'
                    "
                  />
                </v-sheet>

                <span class="song-title">{{ song["title"] }}</span>
              </v-col>
            </v-row>
          </v-container>
        </div>
      </div>
      <div v-else>
        <v-container>
          <h3>Recent outings</h3>
        </v-container>

        <v-container>
          <v-row>
            <v-col
              v-for="(song, index) of songs"
              :key="index"
              cols="6"
              md="2"
              class="col-centered"
            >
              <v-sheet
                @click="toSong(song['id'])"
                class="song-cover"
                @mouseover="currentCase = `${index}`"
                @mouseleave="currentCase = ''"
              >
                <!-- Box content that is only displayed when the mouse is over it -->
                <div v-if="currentCase === `${index}`" class="like-comment">
                  {{ song["nb_likes"] }}
                  <v-icon icon="mdi-heart-outline" class="mr-3" small></v-icon>
                  {{ song["nb_comments"] }}
                  <v-icon icon="mdi-comment-text-outline" small></v-icon>
                </div>
                <img
                  :src="song['song_cover']"
                  alt="Profile picture"
                  :style="
                    currentCase === `${index}` ? 'opacity: 0.4;' : 'opacity: 1;'
                  "
                />
              </v-sheet>

              <span class="song-title">{{ songs[index]["title"] }}</span>
            </v-col>
          </v-row>
        </v-container>
      </div>

      <v-divider></v-divider>

      <v-container class="mt-4">
        <span id="graph-title"><h3>Top 5 most popular genres</h3></span>
        <div>
          <canvas id="myChart"></canvas></div
      ></v-container>
    </v-main>
  </v-app>
</template>

<style scoped>
.like-comment {
  position: absolute;
  display: flex;
  justify-content: center;
  z-index: 1;
}

.col-centered {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.song-cover,
.profile_picture {
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  height: 150px;
  width: 150px;
}

.song-title,
.username {
  display: flex;
  justify-content: center;
  font-size: small;
  margin-top: 0.5em;
}

img {
  background-size: cover;
  background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5));
  height: 150px;
  width: 150px;
}

#graph-title {
  display: flex;
  justify-content: center;
  margin-bottom: 1em;
}
</style>
