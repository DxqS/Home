<template>
  <div id="container">
    <div class="createCourse-infoModule clearfix">

      <div class="infoModule-left" @click="openModule">
        <h1>课程标题(必填)</h1>
        <div>
          <label>课程标题</label>
          <p>{{course.title?course.title:'暂无内容,点击输入'}}</p>
        </div>
        <div>
          <label>副标题</label>
          <p>{{course.subtitle?course.subtitle:'暂无内容,点击输入'}}</p>
        </div>
      </div>

      <div class="js-infoModule-middle all-center" @click="toggleModule"></div>

      <div class="infoModule-right">
        <h1>课程标题(必填)</h1>
        <div>
          <label for="title">课程标题</label>
          <input id="title" type="text" v-model="course.title" placeholder="暂无内容,点击输入" maxlength="10"/>
        </div>
        <div>
          <label for="subTitle">副标题</label>
          <input id="subTitle" type="text" v-model="course.subtitle" placeholder="暂无内容,点击输入" maxlength="10"/>
        </div>
      </div>

    </div>

    <div class="createCourse-infoModule clearfix">
      <div class="infoModule-left" @click="openModule">
        <h1>招生信息</h1>
        <div>
          <label>招生对象</label>
          <p>{{course.enroll_target?course.enroll_target:'暂无内容,点击输入'}}</p>
        </div>
        <div v-if="course.type!='red_on'">
          <label>招生人数</label>
          <p>{{course.enroll_count?course.enroll_count:'暂无内容,点击输入'}}</p>
        </div>
        <div>
          <label>剩余名额</label>
          <p>{{course.rest_count?course.rest_count:'暂无内容,点击输入'}}</p>
        </div>
        <div>
          <label>招生截止</label>
          <p>{{course.enroll_time?course.enroll_time:'暂无内容,点击输入'}}</p>
        </div>
      </div>

      <div class="js-infoModule-middle all-center" @click="toggleModule"></div>

      <div class="infoModule-right">
        <h1>招生信息</h1>
        <div>
          <label for="describe">招生对象</label>
          <input id="describe" type="text" v-model="course.enroll_target" placeholder="适合此课程的发型师人群,15字以内"
                 maxlength="15"/>
        </div>
        <div v-if="course.type!='red_on'">
          <label for="overall" class="overall">招生人数</label>
          <input id="overall" type="number" v-model="course.enroll_count" placeholder="招生总人数"/>
          <span>名</span>
        </div>
        <div>
          <label for="remain_people" class="overall">剩余名额</label>
          <input id="remain_people" type="number" v-model="course.rest_count" placeholder="输入纯数字"/>
          <span>名</span>
        </div>
        <div>
          <label for="deadline">招生截止</label>
          <input id="deadline" type="date" v-model="course.enroll_time"
                 :placeholder="course.enroll_time?course.enroll_time:'请选择日期'"/>
        </div>
      </div>
    </div>

    <div class="createCourse-infoModule clearfix">
      <div class="infoModule-left" @click="openModule">
        <h1>课程信息</h1>
        <div>
          <label>课程价格</label>
          <p>{{course.price?course.price:'暂无内容,点击输入'}}</p>
        </div>
        <div>
          <label>{{timesLabel}}</label>
          <p>{{course.times?course.times:'暂无内容,点击输入'}}</p>
        </div>
        <div>
          <label>{{placeLabel}}</label>
          <p>{{course.place?course.place:'暂无内容,点击输入'}}</p>
        </div>
        <div>
          <label>特别说明</label>
          <p class='intro-show'>{{course.remark?course.remark:'暂无内容,点击输入'}}</p>
        </div>
      </div>
      <div class="js-infoModule-middle all-center" @click="toggleModule"></div>
      <div class="infoModule-right">
        <h1>课程信息</h1>

        <div>
          <label for="price" class="price">课程价格</label>
          <input id="price" type="number" v-model="course.price" placeholder="输入纯数字"/>
          <span>RMB</span>
        </div>

        <div>
          <label for="times" :class="course.type == 'red_on' ? 'times':'day'">{{timesLabel}}</label>
          <input id="times" type="number" v-model="courseTimes" placeholder="输入纯数字"/>
        </div>

        <div>
          <label for="place">{{placeLabel}}</label>
          <input id="place" type="text" v-model="course.place" :placeholder="place_holder" maxlength="15"/>
        </div>

        <div class="intro-container">
          <label for="remark">特别说明</label>
          <textarea id="remark" type="text" v-model="course.remark " rows="2" cols="24"
                    placeholder="不超过40字，包教包会，免费复读等" maxlength="40"></textarea>
        </div>
      </div>
    </div>

    <div class="alert" v-show="courseLimit">
      <div class="cover"></div>
      <div class="popover all-center">
        <section class="alert-content">
          <p>请先填写课程标题</p>
        </section>
        <footer>
          <a href="javascript:;" class="btn" @click="closeWindow">我知道了</a>
        </footer>
      </div>
    </div>

    <div class="createCourse-btns">
      <a href="javascript:;" class="btn btn-border" @click="nextStep">下一页</a>
    </div>
  </div>
</template>

<script>
  import {mapState} from 'vuex'
  import * as types from '../../stores/edu/mutation-types'

  export default{
    data(){
      return {
        courseLimit: false,
      }
    },
    created: function () {
      document.title = this.$route.query.course_id ? '修改课程' : '创建课程'
      refresh_title()
    },
    computed: {
      timesLabel () {
        return this.$store.state.course.type == 'red_on' ? '课程次数' : '课程天数'
      },
      courseTimes: {
        get: function () {
          return this.$store.state.course.times
        },
        // setter
        set: function (newValue) {
          var times = parseInt(newValue)
          this.$store.state.course.times = times
          var slen = this.$store.state.course.schedules.length

          if (slen > 5) {
            if (times < slen) {
              if (times > 5) {
                this.$store.state.course.schedules = this.$store.state.course.schedules.slice(0, times)
              } else {
                this.$store.state.course.schedules = []
              }
            }
          } else {

            if (times < slen) {
              this.$store.state.course.schedules = this.$store.state.course.schedules.slice(0, times)
            } else {
              if (times > 5) {
                this.$store.state.course.schedules = []
              }
            }


          }

        }
      },
      // 使用对象展开运算符将此对象混入到外部对象中
      ...mapState({
        course: state => state.course,
        placeLabel (state) {
          return state.course.type == 'red_on' ? '授课平台' : '授课地点'
        },
        place_holder (state) {
          return state.course.type == 'red_on' ? '微信群/千聊直播/映客直播等' : '输入大概授课地点,16字以内'
        }
      })
    },
    methods: {
      openModule: function (event) {
        $(event.currentTarget).next('.js-infoModule-middle').click()
      },
      toggleModule: function (event) {
        switchModule(event.target)
      },
      nextStep: function () {
        if (this.$store.state.course.title && this.$store.state.course.subtitle) {

          this.$router.push({
            name: 'courseEdit2',
            params: {courseType: this.$route.params.courseType}
          })

        } else {
          this.courseLimit = true
        }
      },
      closeWindow: function () {
        this.courseLimit = false
      }
    },
    beforeRouteEnter (to, from, next) {
      next(function (vm) {
        console.log(from)
        console.log(from.name)
        console.log(vm.$route.query.course_id)

        if (from.name != 'courseEdit2') {
          if (vm.$route.query.course_id > 0) {
            $.post('/course/info/' + vm.$route.query.course_id, function (res) {
              if (res.status == 1) {
                vm.$store.commit(types.INIT_COURSE, res.course)
              }
            }, 'json');
          } else {
            vm.$store.commit(types.INIT_COURSE)
          }
        }

        vm.$store.state.course.type = vm.$route.params.courseType
      })
    },
    beforeRouteLeave (to, from, next) {
      if (to.name != 'courseEdit2') {
        this.$store.commit(types.INIT_COURSE)
      }
      next()
    }
  }
</script>
