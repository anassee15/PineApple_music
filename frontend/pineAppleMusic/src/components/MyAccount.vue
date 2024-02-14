<script lang="ts">
import axios from "axios";
import Navbar from "./Navbar.vue";

export default {
  data: () => ({
    showEditIcon: false,
    editDescBool: false,
    showDesc: true,
    showMusic: true,
    showLikes: true,
    showComments: false,
    showConfirm: false,
    username: "",
    profile_picture: "",
    description: "",
    description_buffer: "",
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
    async deleteSong(song_id: number, song_index: number) {
      // delete song from backend
      // music_index is the index of the song in songs
      await axios
        .delete(`backend/song/${song_id}`, {
          headers: {
            Authorization: `Token ${localStorage.getItem("token")}`,
          },
        })
        .then((response) => {
          this.showConfirm = false;
          // remove song from music for displaying
          this.songs.splice(song_index, 1);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async deleteComment(comment: any, index: number) {
      // delete comment from backend
      // index is the index of the comment in the comments array
      await axios
        .delete(`backend/comment/${comment["id"]}`, {
          headers: {
            Authorization: `Token ${localStorage.getItem("token")}`,
          },
        })
        .then((response) => {
          this.showConfirm = false;
          // remove comment from comments for displaying
          this.comments.splice(index, 1);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async editDesc() {
      // edit description
      try {
        const token = localStorage.getItem("token");

        await axios.patch(
          "backend/users/" + localStorage.getItem("user_id") + "/",
          {
            description: this.description,
          },
          {
            headers: {
              Authorization: `Token ${token}`,
            },
          }
        );

        this.editDescBool = false;
      } catch (error) {
        console.error(error);
      }
    },
    changeEditIcon() {
      this.editDescBool = !this.editDescBool;

      // allow user to edit description, and cancel at any time by clicking the edit icon again
      if (this.editDescBool) {
        this.description_buffer = this.description;
      } else {
        this.description = this.description_buffer;
      }
    },
  },
  async mounted() {
    // get user info
    await axios
      .get(`backend/users/${localStorage.getItem("user_id")}`, {
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
            <v-avatar
              color="black"
              size="120"
              class="profile-avatar-edit"
              @mouseover="showEditIcon = true"
              @mouseout="showEditIcon = false"
            >
              <v-icon
                icon="mdi-pencil"
                color="white"
                v-if="showEditIcon"
              ></v-icon>
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
                    <div v-if="!editDescBool">
                      <p>{{ description }}</p>
                    </div>
                    <div v-else>
                      <v-textarea
                        v-model="description"
                        label="Description"
                        outlined
                        rows="1"
                        auto-grow
                      ></v-textarea>
                      <v-btn color="primary" @click="editDesc">Save</v-btn>
                    </div>
                  </v-card-text>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <div class="edit-desc" @click="changeEditIcon">
                      <v-icon
                        :icon="editDescBool ? 'mdi-pencil-off' : 'mdi-pencil'"
                        class="mr-2"
                      ></v-icon>
                    </div>
                  </v-card-actions>
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

                        <v-icon
                          @click="showConfirm = true"
                          icon="mdi-trash-can-outline"
                          class="ml-2"
                          id="trash-icon"
                          color="red"
                        ></v-icon>
                      </div>

                      <v-dialog
                        v-model="showConfirm"
                        class="elevation-12"
                        max-width="500"
                        dark
                      >
                        <v-card>
                          <v-card-title class="headline"
                            >Confirmation</v-card-title
                          >
                          <v-card-text>
                            <v-icon class="mr-2">mdi-alert</v-icon>
                            Do you really want to delete this song ?
                          </v-card-text>
                          <v-card-actions>
                            <v-btn @click="showConfirm = false"
                              ><v-icon left>mdi-close</v-icon>Cancel</v-btn
                            >
                            <v-btn
                              @click="deleteSong(songs[i - 1]['id'], i - 1)"
                              ><v-icon left>mdi-check</v-icon>Confirm</v-btn
                            >
                          </v-card-actions>
                        </v-card>
                      </v-dialog>
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
                        <v-icon
                          @click="deleteComment(comments[i - 1], i - 1)"
                          icon="mdi-trash-can-outline"
                          class="ml-2"
                          id="trash-icon"
                          color="red"
                        ></v-icon>
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
.profile-avatar-edit {
  position: relative;
}

.profile-avatar-edit:hover {
  cursor: pointer;
}

.profile-avatar-edit i {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  z-index: 1;
}

img:hover {
  opacity: 0.7;
  transition: opacity 0.2ms ease-in-out;
}

.edit-desc {
  cursor: pointer;
}

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

#trash-icon {
  cursor: pointer;
}
</style>
