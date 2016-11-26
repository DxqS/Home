<template>
    <div id="container" class="templateShow-container-bg">
        <section class="templateShow-content" v-show="mark_poster">
            <div class="postShow-image-wrapper templateShow-padding-top">
                <div>
                    <a href="javascript:;" class="postShow-image">
                        <img src="/static/wx/img/6-photo3.jpg" class="all-center" alt="">
                        <span class="post-number">09张</span>
                        <span class="templateShow-label"></span>
                    </a>
                    <p>著名网红制作案例</p>
                </div>
                <div>
                    <a href="javascript:;" class="postShow-image">
                        <img src="/static/wx/img/6-photo4.jpg" alt="">
                        <span class="post-number">09张</span>
                        <span class="templateShow-label online"></span>
                    </a>
                    <p>陈军制作案例</p>
                </div>
            </div>
        </section>
        <section class="templateShow-content"  v-show="mark_page">
            <div class="templateShow-image-wrapper padding-top">
                <div>
                    <a href="javascript:;" class="templateShow-image">
                        <img src="/static/wx/img/6-photo1.jpg" alt="">
                        <span class="templateShow-label"></span>
                    </a>
                    <p>主题1海报模板</p>
                </div>
                <div>
                    <a href="javascript:;" class="templateShow-image">
                        <img src="/static/wx/img/6-photo1.jpg" alt="">
                        <span class="templateShow-label online"></span>
                    </a>
                    <p>主题2海报模板</p>
                </div>
            </div>
        </section>
        <section class="templateShow-bottom-btn">
            <a href="javascript:;" :class="mark_page? 'active': ''"   v-on:click="pageMark" >主页案例</a>
            <a href="javascript:;" :class="mark_poster? 'active': ''"   v-on:click="posterMark">海报案例</a>
        </section>
    </div>
</template>


<script>
  export default{
    data(){
      return {
        mark_page:false,
        mark_poster:true,
      }
    },
    computed: {
    },
    created: function () {
      document.title = '案例展示';
      refresh_title();
    },
    methods: {
      pageMark:function(){
        var vm = this;
        vm.mark_page = true;
        vm.mark_poster = false;

      },
      posterMark: function () {
        var vm = this;
        vm.mark_page = false;
        vm.mark_poster = true;
      },
    },
    beforeRouteEnter (to, from, next) {
      next(function (vm) {
      })
    }
  }

</script>
