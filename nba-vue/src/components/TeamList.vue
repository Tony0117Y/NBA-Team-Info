<template>
  <div>
    <n-layout>
      <n-layout-header style="background-color: #001529; color: white; padding: 20px; text-align: center;">
        <h1>NBA Teams</h1>
      </n-layout-header>

      <n-layout-content style="padding: 20px;">
        <!-- Search Bar -->
        <n-input
          class="search-bar"
          v-model:value="searchQuery"
          placeholder="Search for a team!"
          clearable
          @update:value="filterTeams"
          style="margin-bottom: 20px; width: 100%;"
          
        />

        <!-- Filtered Teams List -->
        <n-card
          class="card"
          v-for="team in filteredTeams"
          :key="team.id"
          style="margin-bottom: 20px;"
          hoverable
        >
          <h2>{{ team.full_name }}</h2>
          <n-button class="button" type="primary" @click="showTeamDetails(team)">View Details</n-button>
        </n-card>

        <!-- No Results Message -->
        <n-card v-if="filteredTeams.length === 0 && searchQuery.trim() !== ''">
          <h2>No teams found for "{{ searchQuery }}"</h2>
        </n-card>
      </n-layout-content>
    </n-layout>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

export default {
  setup() {
    const teams = ref([]);
    const searchQuery = ref("");
    const filteredTeams = ref([]);
    const router = useRouter();

    // Fetch teams with error handling
    const fetchTeams = async () => {
      try {
        const response = await axios.get("https://nba-team-info.onrender.com");
        console.log('API Response:', response.data);
        
        // Validate response structure
        if (!Array.isArray(response.data?.teams)) {
          throw new Error('Invalid teams data format');
        }
        
        teams.value = response.data.teams;
        filteredTeams.value = response.data.teams;
      } catch (error) {
        console.error("Team fetch failed:", error);
        // Fallback data for testing
        teams.value = [
          { id: 1, full_name: "Atlanta Hawks" },
          { id: 2, full_name: "Boston Celtics" },
          { id: 3, full_name: "Chicago Bulls" }
        ];
        filteredTeams.value = teams.value;
      }
    };

    // Simplified filter function
    const filterTeams = () => {
      const query = searchQuery.value.trim().toLowerCase();
      console.log(`Filtering with query: "${query}"`);

      if (!query) {
        filteredTeams.value = teams.value;
        return;
      }

      filteredTeams.value = teams.value.filter(team => 
        team.full_name.toLowerCase().includes(query)
      );

      console.log('Filter Results:', filteredTeams.value);
    };

    const showTeamDetails = (team) => {
      sessionStorage.setItem("selectedTeam", JSON.stringify(team));
      router.push("/teaminfo");
    };

    onMounted(fetchTeams);

    return {
      teams,
      searchQuery,
      filteredTeams,
      filterTeams,
      showTeamDetails,
    };
  },
};
</script>

<style scoped>
.search-bar {
  border-color: #C8102E !important;
}

.button{
  background: #1D428A;
  border-color: #C8102E;
}
.button:hover{
  border-color: #1D428A;
  background: #C8102E;
}
.card {
  border-color: 	#C8102E;
}

h1 {
  margin: 0;
}
</style>