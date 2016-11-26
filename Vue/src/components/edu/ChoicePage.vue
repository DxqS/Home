<template>
  <div id="container" class="templateShow-container-bg">
    <a v-show="no_temp" class="prompt" v-on:click="pageMark">您还没有收藏或使用过任何模板，现在就去<span>模板广场</span>看看吧</a>
    <section class="templateShow-content" v-show="my_show">
      <div class="templateShow-image-wrapper templateShow-padding-top">
        <template v-for="my_page in my_page_list">
          <div>
            <a href="javascript:;" class="templateShow-image">
              <img :src="my_page.img | imgFile('!fw200')" alt="" v-on:click="showPicture">
              <span class="templateShow-label using" v-if="my_page.using==1"></span>
            </a>
            <div class="templateShow-choose-message">
              <p>{{my_page.title}}</p>
              <a href="javascript:;" class="btn btn-border remove-btn" :data-id="my_page._id"
                 v-on:click="removePromptBox">移除</a>
              <a href="javascript:;" class="btn btn-border use-btn" :data-id="my_page._id" v-on:click="usePage">使用</a>
            </div>
          </div>
        </template>
      </div>
    </section>
    <section class="templateShow-content" v-show="mark_show">
      <div class="templateShow-image-wrapper templateShow-padding-top">
        <template v-for="page in page_list">
          <div>
            <a href="javascript:;" class="templateShow-image">
              <img  :src="page.img | imgFile('!fw200')" alt="">
            </a>
            <div class="templateShow-choose-message">
              <p>{{page.title}}</p>
              <a href="javascript:;" class="btn have-btn" v-show="page.follow==1">已收藏</a>
              <a href="javascript:;" class="btn btn-border use-btn" v-show="page.follow==0" :data-id="page._id"
                 v-on:click="collectionPage">收藏</a>
              <a href="javascript:;" class="btn btn-border use-btn" :data-id="page._id" v-on:click="usePage">使用</a>
            </div>
          </div>
        </template>
      </div>
    </section>
    <section class="templateShow-bottom-btn">
      <a href="javascript:;" :class="my_show? 'active': ''" v-on:click="myPage">主页模板</a>
      <a href="javascript:;" :class="mark_show? 'active': ''" v-on:click="pageMark">模板广场</a>
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
                       class="btn" >确定</router-link>
        </footer>
      </div>
    </div>
    <div class="alert" v-show="remove_model">
      <div class="cover"></div>
      <div class="popover all-center">
        <section class="alert-content">
           <p>是否确定要将此模板移除</p>
           <p>移除后可在模板广场中找回</p>
        </section>
        <footer>
          <a href="javascript:;" class="btn btn-cancel" v-on:click="closeWindow">取消</a>
          <a href="javascript:;" class="btn" v-on:click="removePage">确定</a>
        </footer>
      </div>
    </div>
    <div class="alert" v-show="vip_level">
      <div class="cover"></div>
      <div class="popover all-center">
        <section class="alert-content">
          <p>您的VIP特权已到期</p>
          <p>如需使用此模板请先开通VIP会员</p>
        </section>
        <footer>
          <a href="javascript:;" class="btn btn-cancel" v-on:click="closeWindow">取消</a>
          <a href="javascript:;" class="btn" v-on:click="openVIP">确定</a>
        </footer>
      </div>
    </div>
  </div>
</template>

<script>
  export default{
    data(){
      return {
        page_list: [],
        course_id: 0,
        level: 0,
        my_page_list: [],
        num: 0,
        mark_show: false,
        msg_all: false,
        vip_level: false,
        my_show: true,
        remove_model:false,
        course_type: 'org_off',
        div_page: "",
        no_temp: false

      }
    },
    created: function () {
      document.title = '选择主页模板';
      refresh_title();
    },
    methods: {
      pageMark: function () {
        var vm = this;
        vm.page_list = [];
        $.post('/page/list/' + vm.num + '/1', function (res) {
          if (res.status == 1) {
            vm.page_list = res.page_list;
            vm.mark_show = true;
            vm.my_show = false;
            vm.no_temp = false;
          }
        }, 'json');

      },
      myPage: function () {
        var vm = this;
        vm.my_page_list = [];
        $.post('/page/personal/list/' + vm.num + '/1', function (res) {
          if (res.status == 1) {
            vm.my_page_list = res.my_page_list;
            vm.mark_show = false;
            vm.my_show = true;
            if (vm.my_page_list.length == 0) {
              vm.no_temp = true;
            } else {
              vm.no_temp = false;
            }
          }
        }, 'json');

      },
      collectionPage: function (event) {
        var div = $(event.target);
        $.post('/tmp/follow/page/' + div.data("id"), function (res) {
          if (res.status == 1) {
            div.hide();
            div.prev().show();
          }
        }, 'json');
      },
      removePromptBox: function(event){
        var div = $(event.target);
        this.div_page = div;
        this.remove_model = true;
      },
      removePage: function () {
        var div = this.div_page;
        var vm = this;
        $.post('/tmp/remove/page/' + div.data("id"), function (res) {
          if (res.status == 1) {
             vm.remove_model = false,
            div.parent().parent().remove();
          }
        }, 'json');
      },
      usePage: function (event) {
        var vm = this;
        var div = $(event.target);
        $.post('/course/page/set/' + div.data("id"), {'course_id': vm.course_id}, function (res) {
          if (res.status == 1) {
            window.location.href = "/page/course/" + vm.course_id;
          } else {
            if (res.error_code == 30002) {
              vm.vip_level = true;
            } else {
              vm.msg_all = true;
            }
          }
        }, 'json');
      },
      closeWindow: function () {
        this.msg_all = false;
        this.vip_level = false;
        this.remove_model = false;
      },
      openVIP: function () {
        window.location.href = '/wx/index#/pricing';
      },
      showPicture: function (event) {
        var div = $(event.target);
        var img_url = div.attr('src').replace("!fw200","")
        wx.previewImage({
          current: img_url, // 当前显示图片的http链接
          urls: [img_url] // 需要预览的图片http链接列表
        });
      }
    },
    beforeRouteEnter (to, from, next) {
      next(function (vm) {
        vm.course_id = vm.$route.params.courseId;
        vm.num = vm.$route.params.num;
        if (vm.num==5){vm.course_typ="org_off"}else if(vm.num==7){vm.course_typ="red_off"}else{vm.course_typ="red_on"}
        console.log(vm.$route.params, vm.$route.params.num)
        $.post('/page/personal/list/' + vm.num + '/1', function (res) {
          if (res.status == 1) {
            vm.my_page_list = res.my_page_list;
            vm.level = res.level
            if (vm.my_page_list.length == 0) {
              vm.no_temp = true;
            }
          }
        }, 'json');
      })
    }
  }

</script>
