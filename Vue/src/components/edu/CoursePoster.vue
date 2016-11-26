<template>
<div id="container" class="templateShow-container-bg">
        <section class="templateHistory-header" v-show="leng>0">
            <p>历史编辑</p> <router-link :to="{ path: '/courses/'+course_id+'/use/posters/'+poster_id}">更多</router-link>
            <div class="templateHistory-image-wrapper">
              <template v-for="(poster,index) in shares">
                <div class="templateHistory-image-slider" v-if="index<3">
                  <img :src="poster.img | imgFile('!fw200')" class="all-center" alt="">
                </div>
              </template>
            </div>
        </section>
        <section class="templateHistory-header">
            <p>海报模板</p>
        </section>
        <section class="templateShow-content">
            <div class="postShow-image-wrapper">
               <template v-for="(scene, index) in scenes">
                <div>
                    <a href="javascript:;" class="postShow-image" v-on:click="usePoster(index)">
                        <img :src="scene.img | imgFile('!fw200')" class="all-center" alt="">
                    </a>
                    <p>{{scene.title}}</p>
                </div>
                 </template>
            </div>
        </section>
  <div class="alert" v-show="msg_all">
    <div class="cover"></div>
    <div class="popover all-center">
      <section class="alert-content">
        <p>您的课程信息还有未填写内容</p>
        <p>前往课程信息完善所有内容</p>
      </section>
      <footer>
        <a href="javascript:;" class="btn btn-cancel" v-on:click="closeWindow">取消</a>
        <router-link :to="{ path: '/courses/edit/'+course_type+'/e1',query: { course_id: course_id }}"
                     class="btn">确定
        </router-link>
      </footer>
    </div>
  </div>
</div>
</template>

<script>
  export default{
    data(){
      return {
        scenes: [],
        shares: [],
        leng: -1,
        msg_all: false
      }
    },
    created: function () {
      document.title = '课程海报详情页';
      refresh_title();
    },
    computed: {
      leng: function () {
        return this.shares ? this.shares.length : 0
      }
    },
    methods: {
      usePoster:function(index){
         if(parseInt(this.msg_perfect)==0){
           this.msg_all = true;
         }else{
           var num = parseInt(index)+1
           window.location.href="/poster/course/"+this.course_id+"/temp/"+this.poster_id+"/"+num.toString()
         }
      },
      closeWindow: function () {
        this.msg_all = false;
      }
    },
    beforeRouteEnter (to, from, next) {
      next(function (vm) {
        vm.poster_id = vm.$route.params.posterId;
        vm.course_id = vm.$route.params.courseId;
        $.post('/course/poster/info/' + vm.poster_id, {'course_id': vm.course_id}, function (res) {
          if (res.status == 1) {
            vm.scenes = res.poster_list.scenes;
            vm.shares = res.poster_list.share;
            vm.course_type = res.course.type;
            vm.msg_perfect = res.course.msg_perfect;

          }
        }, 'json');
      })
    }
  }
</script>
