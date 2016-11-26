<template>
    <div id="container" class="templateShow-container-bg">
      <a v-show="no_temp" class="prompt" v-on:click="pageMark">您还没有收藏或使用过任何模板，现在就去<span>模板广场</span>看看吧</a>
        <section class="templateShow-content" v-show="my_show">
            <div class="postShow-image-wrapper templateShow-padding-top">
              <template v-for="my_poster in my_poster_list">
                <div>
                  <a href="javascript:;" class="postShow-image">
                     <router-link :to="{ path: '/courses/'+course_id+'/mark/poster/detail/'+my_poster._id}">
                    <img :src="my_poster.img | imgFile('!fw200')" class="all-center" alt=""></router-link>
                    <span class="post-number">{{my_poster.poster_leng}}张</span>
                  </a>
                  <div class="templateShow-choose-message pos">
                    <p>{{my_poster.title}}</p>
                    <a href="javascript:;" class="btn btn-border remove-btn" :data-id="my_poster._id" v-on:click="removePromptBox">移除</a>
                    <a href="javascript:;" class="btn btn-border use-btn" :data-id="my_poster._id" v-on:click="usePage">使用</a>
                  </div>
                </div>
              </template>
            </div>
        </section>
        <section class="templateShow-content" v-show="mark_show">
            <div class="postShow-image-wrapper templateShow-padding-top">
               <template v-for="poster in poster_list">
                <div>
                    <a href="javascript:;" class="postShow-image">
                         <router-link :to="{ path: '/courses/'+course_id+'/mark/poster/detail/'+poster._id}">
                           <img  :src="poster.img | imgFile('!fw200')" alt=""></router-link>
                        <span class="post-number">{{poster.poster_leng}}张</span>
                    </a>
                    <div class="templateShow-choose-message pos">
                        <p>{{poster.title}}</p>
                        <a href="javascript:;" class="btn have-btn"  v-show="poster.follow==1" >已收藏</a>
                        <a href="javascript:;" class="btn btn-border use-btn"  v-show="poster.follow==0" v-on:click="collectionPage" :data-id="poster._id">收藏</a>
                        <a href="javascript:;" class="btn btn-border use-btn" :data-id="poster._id" v-on:click="usePage">使用</a>
                    </div>
                </div>
                 </template>
            </div>
        </section>
        <section class="templateShow-bottom-btn">
            <a href="javascript:;" :class="my_show? 'active': ''"   v-on:click="myPage">海报模板</a>
            <a href="javascript:;" :class="mark_show? 'active': ''" v-on:click="pageMark">海报广场</a>
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
        <div class="alert" v-show="page_all">
        <div class="cover"></div>
        <div class="popover all-center">
          <section class="alert-content">
          <p>您还没有为主页选择模板</p>
          <p>现在就去选择一个合适的模板吧</p>
          </section>
          <footer>
            <a href="javascript:;" class="btn btn-cancel" v-on:click="closeWindow">取消</a>
            <router-link :to="{ path: '/courses/'+ course_id +'/choice/page/'+num}"
                         class="btn">去选择
            </router-link>
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
        poster_list:[],
        course_id: 0,
        level:0,
        my_poster_list: [],
        num:0,
        mark_show:false,
        my_show:true,
        vip_level: false,
        msg_all: false,
        remove_model:false,
        no_temp: false
      }
    },
    created: function () {
      document.title = '选择海报模版';
      refresh_title();
    },
    methods: {
      pageMark:function(){
        var vm = this;
         vm.poster_list = [];
         $.post('/poster/list/'+ vm.num +'/1', function (res) {
          if (res.status == 1) {
            vm.poster_list = res.poster_list;
            vm.mark_show = true;
            vm.my_show = false;
            vm.no_temp = false;
          }
        },'json');

      },
      myPage: function () {
        var vm = this;
        vm.my_poster_list = [];
        $.post('/poster/personal/list/' + vm.num + '/1', function (res) {
          if (res.status == 1) {
            vm.my_poster_list = res.my_poster_list;
            vm.mark_show = false;
            vm.my_show = true;
            if (vm.my_poster_list.length == 0) {
              vm.no_temp = true;
            } else {
              vm.no_temp = false;
            }
          }
        }, 'json');

      },
      collectionPage: function(event){
        var div = $(event.target);
         $.post('/tmp/follow/poster/'+div.data("id"), function (res) {
          if (res.status == 1) {
            div.hide();
            div.prev().show();
          }
        },'json');
      },
      removePage: function(){
        var div = this.div_page;
        var vm = this;
         $.post('/tmp/remove/poster/'+div.data("id"), function (res) {
          if (res.status == 1) {
                vm.remove_model = false,
                div.parent().parent().remove();
          }
        },'json');
      },
      usePage: function(event){
        var vm = this;
        var div = $(event.target);
         $.post('/course/poster/set/'+ div.data("id"),{'course_id':vm.course_id}, function (res) {
            if (res.status == 1) {
              vm.$router.push('/courses/' + vm.course_id + '/poster/' + vm.num)
            }else{
              if (res.error_code == 30002) {
                vm.vip_level = true;
              } else if(res.error_code==30003) {
                vm.page_all = true;
              }else{
                vm.msg_all = true;
              }
            }
         },'json');
      },
      closeWindow: function () {
        this.vip_level = false;
        this.msg_all = false;
        this.remove_model = false;
        this.page_all = false;
      },
      openVIP: function(){
        window.location.href='/wx/index#/pricing';
      },
      removePromptBox: function(event){
        var div = $(event.target);
        this.div_page = div;
        this.remove_model = true;
      },
    },
    beforeRouteEnter (to, from, next) {
        next(function (vm) {
          vm.course_id = vm.$route.params.courseId;
          vm.num =  vm.$route.params.num;
          if (vm.num==5){vm.course_typ="org_off"}else if(vm.num==7){vm.course_typ="red_off"}else{vm.course_typ="red_on"}
          console.log(vm.$route.params,vm.$route.params.num)
          $.post('/poster/personal/list/'+ vm.num +'/1', function (res) {
            if (res.status == 1) {
              vm.my_poster_list = res.my_poster_list;
              vm.level = res.level
              if (vm.my_poster_list.length == 0) {
                vm.no_temp = true;
              }
            }
          },'json');
      })
    }
  }
</script>
