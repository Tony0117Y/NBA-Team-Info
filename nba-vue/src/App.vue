<template>
  <div id="app">
    <router-view />
    <n-button
      v-show="showScrollButton"
      @click="scrollToTop"
      type="primary"
      style="position: fixed; bottom: 20px; right: 20px; z-index: 1000;"
    >
      Back to Top
    </n-button>
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted } from "vue";

export default {
  setup() {
    const showScrollButton = ref(false);

    // Show or hide the button based on scroll position
    const handleScroll = () => {
      showScrollButton.value = window.scrollY > 400; // Show button after scrolling 200px
    };

    // Scroll to the top of the page
    const scrollToTop = () => {
      window.scrollTo({
        top: 0,
        behavior: "smooth", // Smooth scrolling
      });
    };

    onMounted(() => {
      window.addEventListener("scroll", handleScroll);
    });

    onUnmounted(() => {
      window.removeEventListener("scroll", handleScroll);
    });

    return {
      showScrollButton,
      scrollToTop,
    };
  },
};
</script>

<style>
/* Optional: Add custom styles for the button */
</style>