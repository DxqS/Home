<template>
  <div id="container" class="createCourse-container" >
    <template v-if="leng==0">
    <p class="prompt">您还没有创建过任何课程，请点击“创建课程”</p>
    <nav class="createCourse-nav">
      <ul>
        <li><a href="javascript:;" class="course-icon createCourse" v-on:click="addCourse"></a></li>
        <li><a href="javascript:;" class="course-icon how" v-on:click="howCreate"></a></li>
        <li><a href="javascript:;" class="course-icon planShow" v-on:click="courseShow"></a></li>
      </ul>
    </nav>
    </template>
    <template v-if="leng>0">
      <template v-for="(course,index) in courses">
        <nav class="userCenter-nav" :id="index">
          <p class="p-margin-top" :class="course.msg_perfect==1?'end':'not'">{{index+1}}.{{course['title']}}</p>
          <ul data-id="{{course['id']}}">
            <li>
              <a href="javascript:;" class="course-icon courseHome" :data-page="course.page_key" :data-id="course.id"
                 :data-num="course.num"  v-on:click="pageHome"></a>
            </li>
            <li>
              <router-link :to="{ path: '/courses/'+course['id']+'/choice/page/'+course['num']}"
                           class="course-icon changeHome"></router-link>
            </li>
            <li>
              <router-link :to="{ path: '/courses/edit/'+course.type+'/e1',query: { course_id: course['id'] }}"
                           class="course-icon courseInfo"></router-link>
            </li>
            <li>
              <router-link :to="{ path: '/courses/'+course['id']+'/poster/'+course['num']}"
                           class="course-icon createPost"></router-link>
            </li>
          </ul>
          <a href="javascript:;" class="course-icon delete" v-on:click="clickDelete(index,course['id'])"></a>
        </nav>
      </template>
      <a href="javascript:;" class="addCourse-btn" v-on:click="addCourse">加新课程</a>
      <div class="createCourse-bottom-btn">
        <a href="javascript:;" class="course-icon how-on" v-on:click="howCreate"></a>
        <a href="javascript:;" class="course-icon planShow-on" v-on:click="courseShow"></a>
      </div>
      <div class="alert createCourse-alert" v-show="delete_course">
        <div class="cover"></div>
        <div class="popover all-center">
          <section class="alert-content">
            <p>要删除此课程么？</p>
          </section>
          <footer>
            <a href="javascript:;" class="btn cancel-btn" v-on:click="closeWindow">取消</a>
            <a href="javascript:;" class="btn delete-btn" v-on:click="deleteCourse">删除</a>
          </footer>
        </div>
      </div>
    </template>
    <div class="alert createCourse-alert" v-show="add_course">
      <div class="cover"></div>
      <div class="popover all-center">
        <header>
          <a href="javascript:;" class="close" v-on:click="closeWindow">关闭</a>
        </header>
        <section class="alert-content">
          <p>选择要创建的课程</p>
        </section>
        <footer>
          <a href="javascript:;" class="btn" v-on:click="choseAddCourse('red_off')">线下课程</a>
          <a href="javascript:;" class="btn" v-on:click="choseAddCourse('red_on')">网络课程</a>
        </footer>
      </div>
    </div>
    <div class="alert" v-show="msg_all">
      <div class="cover"></div>
      <div class="popover all-center">
        <section class="alert-content">
          <p>您还没有为主页选择模板</p>
          <p>现在就去选择一个合适的模板吧</p>
        </section>
        <footer>
          <a href="javascript:;" class="btn btn-cancel" v-on:click="closeWindow">取消</a>
          <a href="javascript:;" class="btn" v-on:click="homePage">确定</a>
        </footer>
      </div>
    </div>
    <div class="alert" v-show="edu_msg">
      <div class="cover"></div>
      <div class="popover all-center">
        <section class="alert-content">
          <p>您还有未完善的教育信息，为了</p>
          <p>可以正常创建课程，请先完善信息</p>
        </section>
        <footer>
          <a href="javascript:;" class="btn btn-cancel" v-on:click="closeWindow">取消</a>
          <a href="javascript:;" class="btn" v-on:click="perfectMsg">去完善</a>
        </footer>
      </div>
    </div>
  </div>
</template>

<script>
  export default{
    data(){
      return {
        courses: [],
        role: 0,
        delete_course:false,
        add_course: false,
        msg_all: false,
        edu_msg: false,
        tmp_course_id: "0",
        first_show: 1,
        leng:-1,
        course_id: 0,
        num: 0,
        edu_msg_all:0,
        delete_obj: ""


      }
    },
    computed: {
      leng: function () {
        return this.first_show != 1 ? this.courses.length : -1
      }
    },
    created: function () {
      document.title = '我的课程';
      refresh_title();
    },
    methods: {
      addCourse: function(){
        var vm = this;
        if (vm.edu_msg_all==0) {
          vm.edu_msg = true;
        }else
        {
          if (vm.role == 1) {
            console.log(vm.role);
            vm.$router.push('/courses/edit/org_off/e1')
          } else {
            vm.add_course = true;
          }
        }
      },
      clickDelete:function(index_id,course_id){
        this.delete_obj = index_id;
        this.delete_course = true;
        this.tmp_course_id = course_id.toString();
      },
      deleteCourse:function(){
        var vm = this;
        $.post('/course/delete/' + this.tmp_course_id, function (res) {
          if (res.status == 1) {
            vm.delete_course = false;
            $("#"+vm.delete_obj).remove()
            var vm_num = parseInt(vm.delete_obj)
            $('.userCenter-nav').each(function(){
              console.log($(this).attr("id"))
               if(parseInt($(this).attr("id")) > vm_num ){
                 var msg = $(this).find('.p-margin-top').text();
                 msg = msg.toString()
                 var num = parseInt(msg.split('.')[0])-1
                 console.log(msg.replace(msg.split('.')[0]+".",num.toString()+"."))
                 $(this).find('.p-margin-top').html(msg.replace(msg.split('.')[0]+".",num.toString()+"."))
              }
            })
          }
        }, 'json');
      },
      choseAddCourse:function(typ){
        this.$router.push('/courses/edit/'+typ+"/e1")
      },
      closeWindow:function(){
        this.add_course = false;
        this.delete_course = false;
        this.msg_all = false;
        this.edu_msg = false;
      },
      howCreate:function(){
        this.$router.push('/courses/how/create/course')
      },
      courseShow:function(){
        this.$router.push('/courses/show')
      },
      pageHome:function(event){
        var div = $(event.target);
        if (div.data('page') == 1) {
         window.location.href = "/page/course/" + div.data('id');
        } else {
          this.course_id = div.data('id');
          this.num = div.data('num');
          this.msg_all = true;

        }
      },
      homePage:function(){
         this.$router.push('/courses/'+this.course_id+'/choice/page/'+this.num)
      },
      perfectMsg: function(){
        var vm = this;
        if (vm.role == 1) {
          console.log(vm.role);
          window.location.href="/wx/index#/cert/organ/edit";
        } else {
           window.location.href="/wx/index#/cert/netred/edit";
        }
      },
    },
    beforeRouteEnter (to, from, next) {
      next(function (vm) {
        $.post('/course/list', function (res) {
          if (res.status == 1) {
            vm.courses = res.courses;
            vm.role = res.role;
            vm.first_show = 0;
            vm.edu_msg_all = res.edu_msg;
          }
        },'json');
      })
    }
  }

</script>
