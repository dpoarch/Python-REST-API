const vm = new Vue({
  el: '#app',
  data: {
    results: []
  },
  mounted() {
    axios.get("http://api.nytimes.com/svc/topstories/v2/home.json?api-key=your_api_key")
    .then(response => {this.results = response.data.results})
  }
});