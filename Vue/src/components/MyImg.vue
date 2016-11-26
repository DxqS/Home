<template>
  <img :src="src?$store.state.img_domain+src:''">
</template>


<script>
  export default {
    name: 'my-img',
    props: ['src']
  }
</script>
