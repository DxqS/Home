<template>
   <div id="container">
        <section class="createPost-container">
            <p class="prompt" v-if="leng==0">您还没有可以创建海报的模板，点击“添加模板”后，方可创建海报</p>
            <div class="createPost-image-wrapper">
              <template v-for="poster in poster_list">
                <div>
                    <div class="createPost-image">
                        <router-link :to="{ path: '/courses/'+course_id+'/poster/detail/'+poster.id}">
                          <img :src="poster.img | imgFile('!fw200')" alt=""></router-link>
                        <span class="post-number">{{poster.leng}}张</span>
                    </div>
                    <p>{{poster.title}}</p>
                </div>
               </template>
                <div v-show="add_course_btn">
                  <router-link :to="{ path: '/courses/'+course_id+'/choice/poster/'+num}" class="add-postTemplate">
                  </router-link>
                  <p>添加海报模板</p>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
  export default{
    data(){
      return {
        course_id: 0,
        num:0,
        poster_list: [],
        leng:-1,
        first_show: 1,
        add_course_btn: false
      }
    },
    computed: {
      leng: function () {
        return this.first_show!=1 ? this.poster_list.length : -1
      }
    },
    created: function () {
      document.title = '课程海报列表';
      refresh_title();
    },
    methods: {
    },
    beforeRouteEnter (to, from, next) {
      next(function (vm) {
        console.log("22")
        vm.course_id = vm.$route.params.courseId;
        vm.num =  vm.$route.params.num;
        $.post('/course/poster/list/'+ vm.course_id, function (res) {
            if (res.status == 1) {
              console.log("11")
              vm.poster_list = res.poster_list;
              vm.first_show = 0;
              vm.add_course_btn = true
            }
          },'json');
      })
    }
  }
</script>
