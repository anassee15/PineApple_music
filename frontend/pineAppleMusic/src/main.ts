import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

// Router
import { router } from './router'

const vuetify = createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: "dark",
  },
})

createApp(App).use(vuetify).use(router).mount('#app')


// Axios config
import axios from "axios";

axios.defaults.baseURL = "http://localhost:8000/";