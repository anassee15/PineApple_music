<script lang="ts">
import axios from "axios";
import Navbar from "./Navbar.vue";

export default {
  props: {
    id: {
      type: String,
      required: true,
    },
  },
  data: () => ({
    showDesc: true,
    showMusic: true,
    showLikes: true,
    showComments: false,
    username: "",
    profile_picture: "",
    description: "",
    songs: "",
    likes: [],
    likes_id: [],
    comments: "",
  }),
  components: { Navbar },
  methods: {
    toSong(id: number) {
      this.$router.push({ name: "song", params: { id: id } });
    },
  },
  async mounted() {
    // get user info
    await axios
      .get(`backend/users/${this.id}`, {
        headers: {
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      })
      .then((response) => {
        this.username = response["data"]["username"];
        this.description = response["data"]["description"];
        this.profile_picture = response["data"]["profile_picture"];
        this.songs = response["data"]["songs"];
        this.comments = response["data"]["comments"];
        this.likes_id = response["data"]["like_song_id"];
      });

    // get liked songs
    for (let i = 0; i < this.likes_id.length; i++) {
      await axios
        .get(`backend/song/${this.likes_id[i]}`, {
          headers: {
            Authorization: `Token ${localStorage.getItem("token")}`,
          },
        })
        .then((response) => {
          this.likes.push(response["data"]);
        });
    }
  },
};
</script>

<template>
  <v-app class="account-page">
    <Navbar> </Navbar>

    <v-main class="account-content">
      <v-container class="mt-5">
        <v-row>
          <v-col cols="12" class="text-center">
            <v-avatar color="black" size="120">
              <img
                :src="profile_picture"
                class="profile-image-edit"
                alt="Profile picture"
                height="120"
              />
            </v-avatar>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" class="text-center mt-3">
            <h3>{{ username }}</h3>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" class="mt-3">
            <v-card>
              <v-card-actions>
                <h3 class="ml-2">About me</h3>
                <v-spacer></v-spacer>
                <v-btn
                  :icon="showDesc ? 'mdi-chevron-up' : 'mdi-chevron-down'"
                  @click="showDesc = !showDesc"
                ></v-btn>
              </v-card-actions>

              <v-expand-transition>
                <div v-show="showDesc">
                  <v-divider></v-divider>
                  <v-card-text>
                    <p>{{ description }}</p>
                  </v-card-text>
                </div>
              </v-expand-transition>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" class="mt-3">
            <v-card>
              <v-card-actions>
                <h3 class="ml-2">My music</h3>
                <v-spacer></v-spacer>
                <v-btn
                  :icon="showMusic ? 'mdi-chevron-up' : 'mdi-chevron-down'"
                  @click="showMusic = !showMusic"
                ></v-btn>
              </v-card-actions>
              <v-divider></v-divider>
              <div v-show="showMusic">
                <v-list>
                  <div v-if="songs.length > 0">
                    <v-list-item v-for="i of songs.length" :key="i">
                      <div class="my-music-1">
                        <div
                          class="my-music"
                          @click="toSong(songs[i - 1]['id'])"
                        >
                          <img
                            :src="songs[i - 1]['song_cover']"
                            alt="cover"
                            height="50"
                            width="50"
                          />
                          <p class="ml-2">{{ songs[i - 1]["title"] }}</p>
                        </div>
                      </div>
                    </v-list-item>
                  </div>
                  <div v-else>
                    <p class="ml-4">Any music...</p>
                  </div>
                </v-list>
              </div>
            </v-card>
          </v-col>
          <v-col cols="12" class="mt-3">
            <v-card>
              <v-card-actions>
                <h3 class="ml-2">Likes</h3>
                <v-spacer></v-spacer>
                <v-btn
                  :icon="showLikes ? 'mdi-chevron-up' : 'mdi-chevron-down'"
                  @click="showLikes = !showLikes"
                ></v-btn>
              </v-card-actions>
              <v-divider></v-divider>
              <div v-show="showLikes">
                <v-list>
                  <div v-if="likes.length > 0">
                    <v-list-item v-for="i in likes.length" :key="i">
                      <div class="my-likes" @click="toSong(likes[i - 1]['id'])">
                        <img
                          :src="likes[i - 1]['song_cover']"
                          alt="cover"
                          height="50"
                        />
                        <p class="ml-2">{{ likes[i - 1]["title"] }}</p>
                      </div>
                    </v-list-item>
                  </div>
                  <div v-else>
                    <p class="ml-4">Any likes...</p>
                  </div>
                </v-list>
              </div>
            </v-card>
          </v-col>
          <v-col cols="12" class="mt-3">
            <v-card>
              <v-card-actions>
                <h3 class="ml-2">Comments</h3>
                <v-spacer></v-spacer>
                <v-btn
                  :icon="showComments ? 'mdi-chevron-up' : 'mdi-chevron-down'"
                  @click="showComments = !showComments"
                ></v-btn>
              </v-card-actions>
              <v-divider></v-divider>
              <div v-show="showComments">
                <v-list>
                  <div v-if="comments.length > 0">
                    <v-list-item v-for="i in comments.length" :key="i">
                      <div class="my-comments">
                        <pre class="ml-2">{{ comments[i - 1]["text"] }}</pre>
                      </div>
                      <v-divider class="mt-2"></v-divider>
                    </v-list-item>
                  </div>
                  <div v-else>
                    <p class="ml-4">Any Comments...</p>
                  </div>
                </v-list>
              </div>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<style scoped>
.my-music,
.my-likes {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.my-music-1,
.my-comments {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
</style>
