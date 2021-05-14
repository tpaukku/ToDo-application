<template>
  <div>
    <button id="axiosLogin">Login</button>
    <button id="axiosList">Get Todo List</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AxiosButton',
  props: {
    msg: String
  },
  methods: {
    login: function() {
      console.log("login called")
      axios
        .post("http://127.0.0.1:8000/api/v1/dj-rest-auth/login/",
          {"username": "user3", "password": "testpassU3"}
        )
        .then(response => {
          console.log(response.data)
        })
        .catch(error => {
          console.log("Axios ERROR:")
          console.log(error.response.status)
          console.log(error.response.data)
          console.log(error.response.headers)
        })
    },
    getList: function() {
      console.log("getList called")
      axios
        .get("http://127.0.0.1:8000/api/v1/", {
          headers: {
            "Authorization": "Token 09fa4486a38f53fbd30c8d5e230f844d098b1ec0"
          }
        }  
        )
        .then(response => {
          console.log(response.data)
        })
        .catch(error => {
          console.log("Axios ERROR:")
          console.log(error.response.status)
          console.log(error.response.data)
          console.log(error.response.headers)
        })
    }
  },

  mounted() {
    document.getElementById("axiosLogin").addEventListener("click", this.login);
    document.getElementById("axiosList").addEventListener("click", this.getList);
  },

  created() {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
