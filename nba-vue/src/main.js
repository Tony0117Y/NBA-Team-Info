import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

// Import Naive UI 
import naive from "naive-ui";


// Create the Vue app
const app = createApp(App);

// Use plugins
app.use(router); // Vue Router
app.use(naive); // Naive UI


// Mount the app
app.mount("#app");