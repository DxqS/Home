<template>
<div id="container" class="templateShow-container-bg">
        <section class="templateShow-content templateShow-padding-top">
            <div class="postShow-image-wrapper">
               <template v-for="scene in shares">
                <div>
                    <a href="javascript:;" class="postShow-image">
                        <img :src="scene.img | imgFile('!fw200')" class="all-center" alt="" v-on:click="showPicture">
                    </a>
                    <p>{{scene.name}}</p>
                </div>
                 </template>
            </div>
        </section>
    </div>
</template>

<script>
  export default{
    data(){
      return {
        shares: []
      }
    },
    created: function () {
      document.title = '海报列表';
      refresh_title();
    },
    computed: {
    },
    methods: {
      showPicture: function (event) {
        var div = $(event.target);
        var img_url = div.attr('src').replace("!fw200", "")
        wx.previewImage({
          current: img_url, // 当前显示图片的http链接
          urls: [img_url] // 需要预览的图片http链接列表
        });
      }
    },
    beforeRouteEnter (to, from, next) {
      next(function (vm) {
        vm.poster_id = vm.$route.params.posterId;
        vm.course_id = vm.$route.params.courseId;
        $.post('/course/poster/info/' + vm.poster_id, {'course_id': vm.course_id}, function (res) {
          if (res.status == 1) {
            vm.shares = res.poster_list.share;
          }
        }, 'json');
      })
    }
  }
</script>
