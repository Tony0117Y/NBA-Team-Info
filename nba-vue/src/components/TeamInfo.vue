<template>
    <n-layout>
      <n-layout-header style="background-color: #001529; color: white; padding: 20px; text-align: center;">
        <h1>Team Details</h1>
      </n-layout-header>
      <n-layout-content style="padding: 20px;">
        <n-card v-if="team">
          <!-- Team Image -->
          <div v-if="team.image_url" style="text-align: center; margin-bottom: 20px;">
            <img :src="team.image_url" :alt="team.full_name" class="team-logo" />
          </div>
  
          <!-- Team Details -->
          <h2>{{ team.full_name }}</h2>
          <p><strong>Abbreviation:</strong> {{ team.abbreviation }}</p>
          <p><strong>Nickname:</strong> {{ team.nickname }}</p>
          <p><strong>City:</strong> {{ team.city }}</p>
          <p><strong>State:</strong> {{ team.state }}</p>
          <p><strong>Year Founded:</strong> {{ team.year_founded }}</p>
  
          <n-button class="button" type="primary" @click="goBack">Back to Teams</n-button>
        </n-card>
  
        <n-card v-else>
          <h2>Loading team details...</h2>
        </n-card>
      </n-layout-content>
    </n-layout>
  </template>
  
  <script>
  import { ref, onMounted } from "vue";
  import { useRouter } from "vue-router";
  
  export default {
    setup() {
      const router = useRouter();
      const team = ref(null);
  
      // Fetch the team from sessionStorage on mount
      onMounted(() => {
        const storedTeam = sessionStorage.getItem("selectedTeam");
        if (storedTeam) {
          team.value = JSON.parse(storedTeam);
        } else {
          // If no team is found, navigate back to the team list
          router.push("/");
        }
      });
  
      const goBack = () => {
        router.push("/");
      };
  
      return {
        team,
        goBack,
      };
    },
  };
  </script>
  
  <style scoped>
  h1 {
    margin: 0;
  }
  
  /* Team Image Styling */
  .team-logo {
    max-width: 200px;
    max-height: 200px;
    object-fit: contain;
    border: 2px solid #5e5c5c;
    border-radius: 10px;
  }
  
  /* Button Styles */
  .button {
    background: #1D428A;
    border-color: #C8102E;
    color: white;
  }
  
  .button:hover {
    border-color: #1D428A;
    background: #C8102E;
  }
  </style>