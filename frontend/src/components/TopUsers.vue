<script>
const API_URL = `http://127.0.0.1:8000/api/v1/users/`

export default {
  data: () => ({
    data: [],
  }),

  created() {
    this.fetchData()
  },

  methods: {
    async fetchData() {
      this.data = await (await fetch(`${API_URL}`)).json()
      this.data = this.data["users"]
    },
    truncate(v) {
      const newline = v.indexOf('\n')
      return newline > 0 ? v.slice(0, newline) : v
    },
    formatDate(v) {
      return v.replace(/T|Z/g, ' ')
    }
  }
}
</script>

<template>
  <h3>Top Users</h3>
  <ul v-if="data.length > 0">
    <li v-for="{ id, username, fullname } in data" :key="id">
      {{ id }} -> {{ username }} :: {{ fullname }}
    </li>
  </ul>
</template>

<style>
a {
  text-decoration: none;
  color: #42b883;
}
li {
  line-height: 1.5em;
  margin-bottom: 0px;
}
.author,
.date {
  font-weight: bold;
}
</style>
