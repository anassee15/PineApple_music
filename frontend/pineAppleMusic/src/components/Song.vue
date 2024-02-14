<script lang="ts">
import Navbar from "./Navbar.vue";
import axios from "axios";

export default {
  name: "AudioPlayer",
  props: {
    id: {
      type: String,
      required: true,
    },
  },
  data: () => ({
    title: "",
    username: "",
    genre: "",
    song_url: "",
    song_cover: "",
    song_user_id: 0,
    showComment: true,
    nb_comments: 0,
    newComment: "",
    comments: [],
    like: false,
    like_id: -1,
    nb_likes: 0,
    showLyrics: false,
    lyrics: "",
    play: false,
    audioProgress: 0,
    audioPlayer: null as HTMLAudioElement | null,
  }),
  components: { Navbar },
  methods: {
    async submitComment() {
      // post comment to backend
      await axios
        .post(
          "backend/comment/",
          {
            user_id: localStorage.getItem("user_id"),
            song_id: this.id,
            text: this.newComment,
          },
          {
            headers: {
              Authorization: `Token ${localStorage.getItem("token")}`,
            },
          }
        )
        .then((response) => {
          console.log(response);
          this.comments.push(response["data"]);
          // reset comment
          this.newComment = "";
        });
    },
    toUser(id: number) {
      // if user is on their own profile, redirect to account page
      if (id == localStorage.getItem("user_id")) {
        this.$router.push({ name: "account" });
      } else {
        this.$router.push({ name: "profile", params: { id: id } });
      }
    },
    playAudio() {
      this.audioPlayer?.play();
    },
    pauseAudio() {
      this.audioPlayer?.pause();
    },
    seekAudio() {
      this.audioPlayer?.pause();
      if (this.audioPlayer) this.audioPlayer.currentTime = this.audioProgress;
      this.audioPlayer?.play();
    },
    handleTimeUpdate() {
      if (this.audioPlayer) this.audioProgress = this.audioPlayer.currentTime;
    },
    async addLike() {
      // if like exists, delete it
      if (this.like) {
        axios
          .delete(`backend/like/${this.like_id}`, {
            headers: {
              Authorization: `Token ${localStorage.getItem("token")}`,
            },
          })
          .then((response) => {
            this.nb_likes--;
          });
      } else {
        await axios
          .post(
            "backend/like/",
            {
              user_id: localStorage.getItem("user_id"),
              song_id: this.id,
            },
            {
              headers: {
                Authorization: `Token ${localStorage.getItem("token")}`,
              },
            }
          )
          .then((response) => {
            this.like_id = response["data"]["id"];
            this.nb_likes++;
          });
      }

      this.like = !this.like;
    },
  },
  async mounted() {
    this.audioPlayer = this.$refs.audioPlayer as HTMLAudioElement;
    this.audioPlayer?.addEventListener("timeupdate", this.handleTimeUpdate);

    let genre_id; // get genre id to get genre name

    await axios
      .get(`backend/song/${this.id}`, {
        headers: {
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      })
      .then((response) => {
        this.song_cover = response["data"]["song_cover"];
        this.song_url = response["data"]["song_path"];
        this.title = response["data"]["title"];
        this.nb_likes = response["data"]["nb_likes"];
        this.nb_comments = response["data"]["nb_comments"];
        this.comments = response["data"]["comments"];
        this.lyrics = response["data"]["lyrics"];

        // get like id for this song if it exists
        this.like_id = response["data"]["likes"].filter((like) => {
          return (
            like["user_id"] == localStorage.getItem("user_id") &&
            like["song_id"] == this.id
          );
        })[0]?.id;

        // get id of artist of this song
        this.song_user_id = response["data"]["user_id"];
        genre_id = response["data"]["genre"][0];
      });

    // if like id exists, set like to true to display correct icon
    this.like = this.like_id ? true : false;

    // get genre name, if genre id exists
    if (genre_id) {
      await axios
        .get(`backend/genre/${genre_id}`, {
          headers: {
            Authorization: `Token ${localStorage.getItem("token")}`,
          },
        })
        .then((response) => {
          this.genre = response["data"]["name"];
        });
    }

    // get username of artist of this song
    await axios
      .get(`backend/users/${this.song_user_id}`, {
        headers: {
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      })
      .then((response) => {
        this.username = response["data"]["username"];
      });
  },
};
</script>

<template>
  <v-app class="song-page">
    <Navbar> </Navbar>

    <v-main class="song-content">
      <v-container class="song">
        <div class="song-song_cover">
          <img
            :src="song_cover"
            alt="Profile picture"
            height="220"
            width="220"
          />
        </div>

        <div class="song-info">
          <span>{{ genre }}</span>
          <div class="music-name">
            <h2>{{ title }}</h2>
          </div>

          <div class="pseudo" @click="toUser(song_user_id)">
            <h3>{{ username }}</h3>
          </div>

          <div class="audio-content">
            <v-icon
              @click="
                play ? pauseAudio() : playAudio();
                play = !play;
              "
              :icon="play ? 'mdi-pause-circle' : 'mdi-play-circle'"
              size="40"
            ></v-icon>

            <v-icon
              @click="addLike"
              :icon="like ? 'mdi-heart' : 'mdi-heart-outline'"
              :color="like ? 'red' : 'default'"
              size="40"
            ></v-icon>

            <div class="ml-2">
              <h2 :style="like ? { color: 'red' } : { color: '#FFFFFFDE' }">
                {{ nb_likes }}
              </h2>
            </div>
          </div>

          <div class="audio-player">
            <audio ref="audioPlayer" :src="song_url"></audio>
            <div class="mr-2 audio-progress">
              {{ Math.trunc(audioProgress / 60) }}:
              <div v-if="Math.round(audioProgress % 60) < 10">0</div>
              {{ Math.round(audioProgress % 60) }}
            </div>
            <v-slider
              @click="
                seekAudio();
                play = true;
              "
              v-model="audioProgress"
              :disabled="!song_url"
              :max="audioPlayer?.duration ?? 0"
            ></v-slider>
            <div class="ml-2">
              {{ Math.trunc(audioPlayer?.duration / 60) ?? 0 }}:{{
                Math.round(audioPlayer?.duration % 60) ?? 0
              }}
            </div>
          </div>
        </div>
      </v-container>

      <v-container v-show="lyrics.length > 10">
        <v-card class="mb-5" variant="outlined">
          <v-card-text>
            <v-card-actions>
              <div id="lyrics-title">
                <h3>Lyrics</h3>
                <v-spacer></v-spacer>
                <v-btn
                  :icon="showLyrics ? 'mdi-chevron-up' : 'mdi-chevron-down'"
                  @click="showLyrics = !showLyrics"
                ></v-btn>
              </div>
            </v-card-actions>
            <v-expand-transition>
              <div v-show="showLyrics">
                <pre>{{ lyrics }}</pre>
              </div>
            </v-expand-transition>
          </v-card-text>
        </v-card>
      </v-container>

      <v-container class="comments">
        <v-card class="mb-5" variant="outlined">
          <v-card-title>
            <div class="comment-title">
              Comments
              <div>
                <v-icon icon="mdi-comment-text-outline"></v-icon>
                {{ nb_comments }}
              </div>
            </div>
          </v-card-title>
          <v-card-text>
            <v-form class="mt-2">
              <v-text-field
                v-model="newComment"
                label="Write a comment"
              ></v-text-field>
              <v-btn @click="submitComment" color="primary" variant="outlined"
                >Send</v-btn
              >
            </v-form>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                :icon="showComment ? 'mdi-chevron-up' : 'mdi-chevron-down'"
                @click="showComment = !showComment"
              ></v-btn>
            </v-card-actions>

            <div v-show="showComment">
              <v-list>
                <v-list-item v-for="(comment, index) in comments" :key="index">
                  <v-card>
                    <v-card-title
                      @click="toUser(comment['user_id'])"
                      class="pseudo"
                    >
                      {{ comment["username"] }}
                    </v-card-title>
                    <v-card-text>
                      <p>{{ comment["text"] }}</p>
                    </v-card-text>
                  </v-card>
                  <v-divider></v-divider>
                </v-list-item>
              </v-list>
            </div>
          </v-card-text>
        </v-card>
      </v-container>
    </v-main>
  </v-app>
</template>

<style scoped>
.song {
  display: flex;
}
.song-page {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.song-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 1.5em;
  min-width: 200px;
  max-width: 800px;
  width: 100%;
}

.audio-player {
  display: flex;
  align-items: baseline;
  min-width: 200px;
  max-width: 600px;
}
.audio-progress {
  display: flex;
  flex-direction: row;
}

.audio-content,
#lyrics-title {
  display: flex;
  align-items: center;
}

.comments {
  min-width: 800px;
  max-width: 1000px;
}

.comment-title {
  display: flex;
  justify-content: space-between;
}

.pseudo {
  cursor: pointer;
}

@media (max-width: 830px) {
  .song {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .song-content {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  .song-info {
    width: 100%;
  }

  .comments {
    min-width: 500px;
  }

  @media screen and (max-width: 550px) {
    .comments {
      min-width: 100%;
      max-width: 100%;
    }
  }
}
</style>
