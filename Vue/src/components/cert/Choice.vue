<template>
<div id="app">
    <div id="container" class="certification">
        <div class="play-video">
            <!-- 视频封面, 使用图片修改poster属性 -->
            <video id="really-cool-video" class="video-js vjs-default-skin" controls
                   preload="none" poster="/static/img/cert_pre.png"
                   data-setup='{}'>
                <!-- 当接受到视频网址数据 -->
                <source src="http://shejiimg.yanzijia.cn/ruherenzheng.mp4" type="video/mp4">
                <!-- 修改上面的src -->
            </video>
        </div>
        <div class="sort-question-list">
            <div class="sort-question-item">
                为何要选择认证分类？
            </div>
            <div class="sort-question-item">
                认证分哪几类？都有什么好处和用途？
            </div>
            <div class="sort-question-item">
                如何去认证？怎么才能保证认证通过？
            </div>
        </div>
        <p class="prompt">
            带着这些问题，仔细看视频，你会得到你想要的的答案！
        </p>
        <div class="next-btn-group">
            <router-link to="/cert/netred" class="btn btn-border">
                认证网红
            </router-link>
            <router-link to="/cert/organ" class="btn btn-border">
                认证教育机构
            </router-link>
        </div>
    </div>
</div>
</template>

<script>
  export default{
    data(){
      return {
        avatar: '',
        nickname: '',
        sex: 0,
        show_edu_bar: false
      }
    },
    created: function () {
      document.title = '认证分类';
      refresh_title();
    },
    methods: {
      edu_bar: function () {
        console.log("edu_bar::" + this.show_edu_bar)
        this.show_edu_bar = !this.show_edu_bar;
        return false;
      }
    },
  }
</script>
