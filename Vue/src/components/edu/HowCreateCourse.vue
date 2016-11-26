<template>
  <div id="container" class="certification">
    <div class="play-video">
      <!-- 视频封面, 使用图片修改poster属性 -->
      <video id="really-cool-video" class="video-js vjs-default-skin" controls
             preload="none" poster="http://shejiimg.yanzijia.cn/manager/temp_page/20161125/b11491589b208a49"
             data-setup='{}'>
        <!-- 当接受到视频网址数据 -->
        <source src="http://shejiimg.yanzijia.cn/chuangjianjiaocheng.mp4" type="video/mp4">
        <!-- 修改上面的src -->
      </video>
    </div>
    <div class="sort-question-list">
      <div class="sort-question-item">
        创建课程有什么用途？有哪些好处？
      </div>
      <div class="sort-question-item">
        如何创建课程？
      </div>
      <div class="sort-question-item">
        如何玩转课程？如何游刃有余的应用？
      </div>
      <div class="sort-question-item">
        创建课程之后如何创建海报？
      </div>
      <div class="sort-question-item">
        海报有何用途？有哪些好处？
      </div>
    </div>
    <p class="prompt">
      带着这些问题，仔细看视频，你会得到你想要的的答案！
    </p>
  </div>
</template>

<script>
  export default{
    data(){
      return {}
    }, created: function () {
      document.title = '如何创建课程';
      refresh_title();
    },
    beforeRouteEnter (to, from, next) {
      next(function (vm) {
      })
    }
  }
</script>
