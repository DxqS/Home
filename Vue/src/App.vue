<template>
  <div id="app">
    <img src="./assets/logo.png">
    <hello></hello>
  </div>
</template>

<script>
  import Hello from './components/Hello'

  export default {
    data(){
      return {
        num: 1
      }
    },
    computed: {
      count(){
        return this.num + 1
      }
    },
    components: {
      Hello
    },
    methods: {
      method: function () {
        return false;
      }
    },
    filters: {
      ff: function (value) {
        return 'filters:' + value
      }
    },
    created: function () {
      document.title = '个人中心';
      refresh_title();
    },
    updated: function () {
      document.title = '个人中心';
      refresh_title();
    },
    beforeRouteEnter (to, from, next) {
      next(function (vm) {

      })
    },
    beforeRouteLeave (to, from, next) {
      next()
    }
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
