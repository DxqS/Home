<template>
      <div id="container" class="templateShow-container-bg">
          <section class="templateShow-content" v-show="page_mark">
            <div class="templateShow-image-wrapper templateShow-padding-top">
               <template v-for="page in page_list">
              <div>
                <a href="javascript:;" class="templateShow-image">
                  <img  :src="page.img | imgFile('!fw200')" alt="" v-on:click="showPicture">
                  <span class="templateShow-label" :class="page.course_typ=='on'? 'online':''"></span>
                </a>
                <div class="templateShow-choose-message">
                  <p>{{page.title}}</p>
                  <a href="javascript:;" class="btn have-btn" v-show="page.follow==1">已收藏</a>
                  <a href="javascript:;" class="btn btn-border use-btn" v-show="page.follow==0" :data-id="page._id"
                     v-on:click="collectionPage" data-typ="page">收藏</a>
                  <a href="javascript:;" class="btn btn-border use-btn" :data-level="page.level" :data-id="page._id"  :data-typ="page.type" v-on:click="usePage($event,'page')">使用</a>
                </div>
              </div>
               </template>
            </div>
          </section>
          <section class="templateShow-content" v-show="poster_mark">
            <div class="postShow-image-wrapper templateShow-padding-top">
               <template v-for="poster in poster_list">
                <div>
                    <a href="javascript:;" class="postShow-image">
                      <router-link :to="{ path: '/courses/0/mark/poster/detail/'+poster._id}">
                        <img :src="poster.img | imgFile('!fw200')" alt="">
                        <span class="templateShow-label label-big" :class="poster.course_typ=='on'? 'online':''"></span>
                        <span class="post-number">{{poster.poster_leng}}张</span>
                      </router-link>
                    </a>
                    <div class="templateShow-choose-message pos">
                        <p>{{poster.title}}</p>
                        <a href="javascript:;" class="btn have-btn"  v-show="poster.follow==1">已收藏</a>
                        <a href="javascript:;" class="btn btn-border use-btn" v-show="poster.follow==0" v-on:click="collectionPage"
                           :data-id="poster._id" data-typ="poster">收藏</a>
                        <a href="javascript:;" class="btn btn-border use-btn" :data-level="poster.level" :data-id="poster._id" :data-typ="poster.type" v-on:click="usePage($event,'poster')">使用</a>
                    </div>
                </div>
                  </template>
            </div>
          </section>
        <section class="templateShow-bottom-btn">
            <a href="javascript:;" :class="page_mark? 'active': ''"   v-on:click="pageMark">主页模板广场</a>
            <a href="javascript:;" :class="poster_mark? 'active': ''"   v-on:click="posterMark">海报模板广场</a>
        </section>
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
  <div class="alert" v-show="no_course">
    <div class="cover"></div>
    <div class="popover all-center">
      <section class="alert-content">
        <p>将模板添加到课程中才可以使用</p>
        <p>您还没有对应的课程</p>
      </section>
      <footer>
        <a href="javascript:;" class="btn btn-cancel" v-on:click="closeWindow">取消</a>
        <router-link :to="{ path: '/courses'}" class="btn">创建课程</router-link>
      </footer>
    </div>
  </div>
  <div class="alert" v-show="chose_course">
    <div class="cover"></div>
    <div class="popover all-center">
      <section class="alert-content-input">
        <p v-show="btn_one">先选择课程才可以使用模板</p>
        <p v-show="btn_two">该课程还没有完善信息</p>
        <p v-show="btn_three">该课程未生成主页，去课程主页查看</p>
        <div class="select-border">
          <span>点击选择适合此模板的课程</span>
          <select name="course" v-model="course_id" id="course" v-on:change="selectCourse">
            <option value="0">点击选择适合此模板的课程</option>
            <template v-for="course in courses">
              <option :data-key="course.page_key" :data-msg="course.msg_perfect" :value="course._id">
                {{course.info.title}}
              </option>
            </template>
          </select>
        </div>
      </section>
      <footer>
        <a href="javascript:;" class="btn btn-cancel" v-on:click="closeWindow">取消</a>
        <a href="javascript:;" class="btn" v-show="btn_one" v-on:click="sureUse">确定</a>
        <router-link :to="{ path: '/courses'}" class="btn" v-show="btn_two">去完善</router-link>
        <router-link :to="{ path: '/courses'}" class="btn" v-show="btn_three">确定</router-link>
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
        poster_list: [],
        page_mark: true,
        poster_mark: false,
        vip_level: false,
        no_course:false,
        chose_course:false,
        btn_one: true,
        btn_two: false,
        btn_three: false,
        roleType: 5,
        level: 0,
        course_id: 0,
        temp_id : 0,
        use_tmp_typ: "",
        courses: [],
        save_courses:[]
      }
    },
    created: function () {
      document.title = '模板广场';
      refresh_title();
    },
    methods: {
      usePage: function(event,typ){
        var div = $(event.target);
        var vm = this;
        vm.courses =[];
        vm.use_tmp_typ = typ;
        console.log(typ)
        vm.temp_id = div.data('id');
        if (vm.level < div.data('level')) {
          vm.vip_level = true;
        } else {
          var course_list = vm.save_courses
          var course_leng = 0
          var new_course_list = []
          for (var i=0;i<course_list.length;i++){
            console.log(div.data("typ"))
            if (course_list[i]["type"]==div.data("typ")){
              course_leng =  course_leng + 1;
              new_course_list.push(course_list[i])
            }
          }
          if (course_leng > 0) {
            $('.select-border span').text("点击选择适合此模板的课程");
            vm.courses = new_course_list;
            vm.course_id = 0;
            this.btn_one = true;
            this.btn_two = false;
            this.btn_three = false;
            vm.chose_course = true;
          } else {
            vm.no_course = true;
          }
        }
      },
      collectionPage: function(event){
        var div = $(event.target);
         $.post('/tmp/follow/'+ div.data('typ')+'/'+div.data("id"), function (res) {
          if (res.status == 1) {
            div.hide();
            div.prev().show();
          }
        },'json');
      },
      pageMark: function(){
        var vm = this;
        vm.page_list = [];
        $.post('/page/list/' + vm.roleType + '/1', function (res) {
          if (res.status == 1) {
            vm.page_list = res.page_list;
            vm.page_mark=true;
            vm.poster_mark= false;
            vm.level = res.level;
          }
        }, 'json');
      },
      posterMark: function(){
        var vm = this;
        vm.poster_list = [];
        $.post('/poster/list/' + vm.roleType + '/1', function (res) {
          if (res.status == 1) {
            vm.poster_list = res.poster_list;
            vm.page_mark=false;
            vm.poster_mark= true;
            vm.level = res.level;
          }
        }, 'json');
      },
      closeWindow: function () {
        this.vip_level = false;
        this.no_course = false;
        this.chose_course = false;
      },
      openVIP: function(){
        window.location.href='/wx/index#/pricing';
      },
      selectCourse:function(){
        var getSelect = $('#course option:selected');
        $('.select-border span').text(getSelect.text());
        if(this.course_id!=0){
        if (getSelect.data("msg") == "" || getSelect.data("msg") == 0 || getSelect.data("msg")==undefined) {
          this.btn_one = false;
          this.btn_two=true;
          this.btn_three = false;
          return false;
        }
        if (this.use_tmp_typ == "poster" && (getSelect.data("key") == "" || getSelect.data("key")==undefined)) {
          this.btn_one = false;
          this.btn_two = false;
          this.btn_three = true;
          return false;
        }
        } else {
          this.btn_one = true;
          this.btn_two = false;
          this.btn_three = false;
        }
      },
      sureUse: function(){
        var vm = this;
        if (vm.course_id !=0 ) {
          if (vm.use_tmp_typ == "page") {
            $.post('/course/page/set/' + vm.temp_id, {'course_id': vm.course_id}, function (res) {
              if (res.status == 1) {
                window.location.href = "/page/course/" + vm.course_id;
              }
            }, 'json');
          } else {
             $.post('/course/poster/set/'+ vm.temp_id,{'course_id':vm.course_id}, function (res) {
                if (res.status == 1) {
                  vm.$router.push('/courses/' + vm.course_id + '/poster/' + vm.roleType)
                }
             },'json');
          }
        }
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
        vm.roleType = vm.$route.params.roleType;
        console.log(vm.$route.params.roleType)
        $.post('/page/list/'+ vm.roleType +'/1',{"have_course":1}, function (res) {
          if (res.status == 1) {
            vm.page_list = res.page_list;
            vm.level = res.level;
            vm.courses = res.courses;
            vm.save_courses = res.courses;
          }
        },'json');
      })
    }
  }
</script>
