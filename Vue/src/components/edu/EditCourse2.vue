<template>
  <div id="container">

    <div class="createCourse-infoModule clearfix" v-if="course.type=='org_off'">
      <div class="infoModule-left infoModule-left-two" @click="openModule">
        <h1>主讲人介绍</h1>
        <aside>
          <!--class=id-photo-->
          <img class="id-photo" :src="course.talker_pic | imgFile('!fw200')" alt="avatar" v-show="course.talker_pic">
        </aside>
        <section>
          <div>
            <label>姓名</label>
            <p>{{course.talker_name?course.talker_name:'暂无内容,点击输入'}}</p>
          </div>
          <div>
            <label>擅长技法</label>
            <p>{{course.talker_skill?course.talker_skill:'暂无内容,点击输入'}}</p>
          </div>
          <div>
            <label>导师职务</label>
            <p>{{course.talker_title?course.talker_title:'暂无内容,点击输入'}}</p>
          </div>
          <div>
            <label>累计学员</label>
            <p>{{course.stu_count?course.stu_count:'暂无内容,点击输入'}}</p>
          </div>
          <div class='intro-show'>
            <label>个人简介</label>
            <p>{{course.talker_intro?course.talker_intro:'暂无内容,点击输入'}}</p>
          </div>
        </section>
      </div>
      <div class="js-infoModule-middle all-center" @click="toggleModule"></div>
      <div class="infoModule-right infoModule-right-two">
        <h1>主讲人介绍</h1>
        <aside @click="up_img($event,'talker_pic')">
          <img class="id-photo" :src="course.talker_pic | imgFile('!fw200')" alt="avatar" v-show="course.talker_pic">
        </aside>
        <section>
          <div>
            <label for="name">姓名</label>
            <input id="name" type="text" v-model.lazy="course.talker_name" placeholder="中英文名字都可以" maxlength="8"/>
          </div>
          <div>
            <label for="tech">擅长技法</label>
            <input id="tech" type="text" v-model.lazy="course.talker_skill" placeholder="8字以内" maxlength="8"/>
          </div>
          <div>
            <label for="post">导师职务</label>
            <input id="post" type="text" v-model.lazy="course.talker_title" placeholder="在学院内担任的职务" maxlength="8"/>
          </div>
          <div>
            <label for="count" class="people">累计学员</label>
            <input id="count" type="number" v-model.lazy="course.stu_count" placeholder="输入纯数字"/>
          </div>
        </section>
        <footer>
          <div class="clearfix">
            <label for="intro">个人简介</label>
            <textarea id="intro" maxlength="50" v-model.lazy="course.talker_intro" placeholder="输入内容,不得超过50字"
                      rows="2" cols="24" maxlength="50"></textarea>
          </div>
        </footer>
      </div>
    </div>

    <div class="createCourse-infoModule clearfix" v-if="course.type!='org_off'">
      <div class="infoModule-left infoModule-left-two" @click="openModule">
        <h1>主讲人介绍</h1>
        <aside>
          <!--class=id-photo-->
          <img class="id-photo" :src="course.talker_pic | imgFile('!fw200')" alt="avatar" v-show="course.talker_pic">
        </aside>
        <section>
          <div>
            <label>姓名</label>
            <p>{{course.talker_name?course.talker_name:'暂无内容,点击输入'}}</p>
          </div>
          <div>
            <label>擅长技法</label>
            <p>{{course.talker_skill?course.talker_skill:'暂无内容,点击输入'}}</p>
          </div>
          <div>
            <label>培训人数</label>
            <p>{{course.stu_count?course.stu_count:'暂无内容,点击输入'}}</p>
          </div>
          <div>
            <label>粉丝数</label>
            <p>{{course.fans_count?course.fans_count:'暂无内容,点击输入'}}</p>
          </div>
          <div>
            <label>开课期数</label>
            <p>{{course.class_count?course.class_count:'暂无内容,点击输入'}}</p>
          </div>
          <div class="intro-show">
            <label>个人简介</label>
            <p>{{course.talker_intro?course.talker_intro:'暂无内容,点击输入'}}</p>
          </div>
          <div>
            <label>二维码</label>
            <p v-show="!course.talker_qrcode">未上传</p>
            <p v-show="course.talker_qrcode">已上传</p>
          </div>
        </section>
      </div>
      <div class="js-infoModule-middle all-center" @click="toggleModule"></div>
      <div class="infoModule-right infoModule-right-two">
        <h1>主讲人介绍</h1>
        <aside @click="up_img($event,'talker_pic')">
          <img class="id-photo" :src="course.talker_pic | imgFile('!fw200')" alt="avatar" v-show="course.talker_pic">
        </aside>
        <section>
          <div>
            <label for="name">姓名</label>
            <input id="name" type="text" v-model.lazy="course.talker_name" placeholder="中英文名字都可以" maxlength="8"/>
          </div>
          <div>
            <label for="tech">擅长技法</label>
            <input id="tech" type="text" v-model.lazy="course.talker_skill" placeholder="8字以内" maxlength="8"/>
          </div>
          <div>
            <label for="count" class="people">累计学员</label>
            <input id="count" type="number" v-model.lazy="course.stu_count" placeholder="输入纯数字"/>
          </div>
          <div>
            <label for="fans">粉丝数</label>
            <input id="fans" type="number" v-model.lazy="course.fans_count" placeholder="输入纯数字"/>
          </div>
        </section>
        <footer>
          <div>
            <label for="courseCount">开课期数</label>
            <input id="courseCount" type="number" v-model.lazy="course.class_count" placeholder="输入纯数字"/>
          </div>
          <div class="clearfix">
            <label for="intro">个人简介</label>
            <textarea id="intro" maxlength="50" v-model.lazy="course.talker_intro" placeholder="输入内容,不得超过50字"
                      rows="2" cols="24"></textarea>
          </div>
          <div>
            <label>二维码</label>
            <div class="qrCode-upload-border" @click="up_img($event,'talker_qrcode')">
              <img :src="course.talker_qrcode | imgFile('!fw200')" v-show="course.talker_qrcode">
            </div>
            <p class="p-center">点击上传微信二维码</p>
          </div>
        </footer>
      </div>
    </div>

    <div class="createCourse-infoModule clearfix" id="J-bright">
      <div class="infoModule-left infoModule-left-two" @click="openModule">
        <h1>课程亮点</h1>
        <div>
          <label>核心亮点</label>
          <p class='intro-show'>{{course.advantage?course.advantage:'暂无内容,点击输入'}}</p>
        </div>
        <div>
          <label>课程标签</label>
          <p class='intro-show'>{{tag_str?tag_str:'暂无内容,点击输入'}}</p>
        </div>
      </div>
      <div class="js-infoModule-middle all-center" @click="toggleModule"></div>
      <div class="infoModule-right infoModule-right-two">
        <h1>课程亮点</h1>
        <div>
          <label for="describe">核心亮点</label>
          <input id="describe" type="text" :value="course.advantage" placeholder="简短介绍课程的亮点" maxlength="15"/>
        </div>
        <div class="right-tag">
          <label class="tag-label">课程标签</label>
          <div v-for="n in 7">
            <label :for="'_'+n">{{n}}.</label>
            <input :id="'_'+n" type="text" :value="n<=course.tags.length?course.tags[n-1]:''"
                   maxlength="4" placeholder="四字以内"/>
          </div>
        </div>
      </div>
    </div>

    <div class="createCourse-infoModule clearfix" id="J-schedules">

      <div class="infoModule-left infoModule-left-two" @click="openModule">
        <h1 class="plan-title">课程安排</h1>
        <div class="left-plan lessOrEqual" v-if="course.times<=5 && course.type !='red_on'">
          <section class="plan-day" v-for="(sche, index) in course.schedules">
            <h2>
              <label>第{{index+1}}{{course.type|timeLable}}</label>
              <p>{{sche.date}}</p>
            </h2>
            <div>
              <label>上午</label>
              <p>{{sche.am.start}}</p>
              <p>{{sche.am.end}}</p>
              <p>{{sche.am.speaker}}</p>
              <p>{{sche.am.intro}}</p>
            </div>
            <div>
              <label>下午</label>
              <p>{{sche.pm.start}}</p>
              <p>{{sche.pm.end}}</p>
              <p>{{sche.pm.speaker}}</p>
              <p>{{sche.pm.intro}}</p>
            </div>
            <div>
              <label>晚上</label>
              <p>{{sche.nt.start}}</p>
              <p>{{sche.nt.end}}</p>
              <p>{{sche.nt.speaker}}</p>
              <p>{{sche.nt.intro}}</p>
            </div>
          </section>
        </div>

        <div class="left-plan moreThan" v-if="course.times>5 || course.type =='red_on'">
          <section class="plan-day" v-for="(sche, index) in course.schedules">
            <h2>
              <label>第{{index+1}}{{course.type|timeLable}}</label>
              <p>{{sche.date}}</p>
            </h2>
            <div>
              <p>{{sche.start}}</p>
              <p>{{sche.end}}</p>
              <p>{{sche.speaker}}</p>
              <p>{{sche.intro}}</p>
            </div>
          </section>
        </div>
      </div>

      <div class="js-infoModule-middle all-center" @click="toggleModule"></div>

      <div class="infoModule-right infoModule-right-two">
        <h1 class="plan-title">课程安排</h1>

        <div class="right-plan lessOrEqual" v-if="course.times<=5 && course.type !='red_on'">

          <section class="plan-day" v-for="(sche, index) in course.schedules">
            <h2>
              <label>第{{index+1}}{{course.type|timeLable}}</label>
              <input class="deadline" type="date" v-model="sche.date"
                     :placeholder="sche.date?sche.date:'请选择日期'"/>
            </h2>
            <div class="am">
              <label>上午</label>
              <select>
                <option value="">开始时间</option>
                <option v-for="n in 6" :selected="(n+6)+':00'==sche.am.start?'selected':''">{{n+6}}:00</option>
              </select>
              <select>
                <option value="">结束时间</option>
                <option v-for="n in 6" :selected="(n+6)+':00'==sche.am.end?'selected':''">{{n+6}}:00</option>
              </select>
              <input type="text" :value="sche.am.speaker" placeholder="讲师姓名" maxlength="5"/>
              <textarea placeholder="简述课程内容,15字以内" rows="2" cols="24" maxlength="15">{{sche.am.intro}}</textarea>
            </div>

            <div class="pm">
              <label>下午</label>
              <select>
                <option value="">开始时间</option>
                <option v-for="n in 6" :selected="(n+12)+':00'==sche.pm.start?'selected':''">{{n+12}}:00</option>
              </select>
              <select>
                <option value="">结束时间</option>
                <option v-for="n in 6" :selected="(n+12)+':00'==sche.pm.end?'selected':''">{{n+12}}:00</option>
              </select>
              <input type="text" :value="sche.pm.speaker" placeholder="讲师姓名" maxlength="5"/>
              <textarea placeholder="简述课程内容,15字以内" rows="2" cols="24" maxlength="15">{{sche.pm.intro}}</textarea>
            </div>

            <div class="nt">
              <label>晚上</label>
              <select>
                <option value="">开始时间</option>
                <option v-for="n in 6" :selected="(n+18)+':00'==sche.nt.start?'selected':''">{{n+18}}:00</option>
              </select>
              <select>
                <option value="">结束时间</option>
                <option v-for="n in 6" :selected="(n+18)+':00'==sche.nt.end?'selected':''">{{n+18}}:00</option>
              </select>
              <input type="text" :value="sche.pm.speaker" placeholder="讲师姓名" maxlength="5"/>
              <textarea placeholder="简述课程内容,15字以内" rows="2" cols="24" maxlength="15">{{sche.nt.intro}}</textarea>
            </div>
          </section>

          <section class="plan-day" v-for="n in course.times-course.schedules.length">
            <h2>
              <label>第{{n+course.schedules.length}}{{course.type|timeLable}}</label>
              <input class="deadline" type="date" placeholder="请选择日期" @change="dateinp"/>
            </h2>
            <div class="am">
              <label>上午</label>
              <select>
                <option value="">开始时间</option>
                <option v-for="n in 6">{{n+6}}:00</option>
              </select>
              <select>
                <option value="">结束时间</option>
                <option v-for="n in 6">{{n+6}}:00</option>
              </select>
              <input type="text" placeholder="讲师姓名" maxlength="5"/>
              <textarea placeholder="简述课程内容,15字以内" rows="2" cols="24" maxlength="15"></textarea>
            </div>
            <div class="pm">
              <label>下午</label>
              <select>
                <option value="">开始时间</option>
                <option v-for="n in 6">{{n+12}}:00</option>
              </select>
              <select>
                <option value="">结束时间</option>
                <option v-for="n in 6">{{n+12}}:00</option>
              </select>
              <input type="text" placeholder="讲师姓名" maxlength="5"/>
              <textarea placeholder="简述课程内容,15字以内" rows="2" cols="24" maxlength="15"></textarea>
            </div>
            <div class="nt">
              <label>晚上</label>
              <select>
                <option value="">开始时间</option>
                <option v-for="n in 6">{{n+18}}:00</option>
              </select>
              <select>
                <option value="">结束时间</option>
                <option v-for="n in 6">{{n+18}}:00</option>
              </select>
              <input type="text" placeholder="讲师姓名" maxlength="5"/>
              <textarea placeholder="简述课程内容,15字以内" rows="2" cols="24" maxlength="15"></textarea>
            </div>
          </section>

        </div>

        <div class="right-plan moreThan" v-if="course.times>5 || course.type =='red_on'">

          <section class="plan-day" v-for="(sche, index) in course.schedules">
            <h2>
              <label>第{{index+1}}{{course.type|timeLable}}</label>
              <input type="date" class="deadline" v-model="sche.date"
                     :placeholder="sche.date?sche.date:'请选择日期'"/>
            </h2>
            <div>
              <select>
                <option value="">开始时间</option>
                <option v-for="n in 15" :selected="(n+6)+':00'==sche.start?'selected':''">{{n+6}}:00</option>
              </select>
              <select>
                <option value="">结束时间</option>
                <option v-for="n in 15" :selected="(n+6)+':00'==sche.end?'selected':''">{{n+6}}:00</option>
              </select>
              <input type="text" :value="sche.speaker" placeholder="讲师姓名" maxlength="5"/>
              <textarea placeholder="简述课程内容,15字以内">{{sche.intro}}</textarea>
            </div>
          </section>

          <section class="plan-day" v-for="n in course.times-course.schedules.length">
            <h2>
              <label>第{{n+course.schedules.length}}{{course.type|timeLable}}</label>
              <input type="date" class="deadline" placeholder="点击选择日期" @change="dateinp"/>
            </h2>
            <div>
              <select>
                <option value="">开始时间</option>
                <option v-for="n in 15">{{n+6}}:00</option>
              </select>
              <select>
                <option value="">结束时间</option>
                <option v-for="n in 15">{{n+6}}:00</option>
              </select>
              <input type="text" placeholder="讲师姓名" maxlength="5"/>
              <textarea placeholder="简述课程内容,15字以内" rows="2" cols="24" maxlength="15"></textarea>
            </div>
          </section>

        </div>

      </div>

    </div>

    <div class="createCourse-btns">

      <a @click="change_page('courseEdit1')" class="btn btn-border">上一页</a>
      <a @click="change_page('courseEdit3')" class="btn btn-border">下一页</a>

    </div>
  </div>
</template>

<script>
  import {mapState} from 'vuex'
  import * as types from '../../stores/edu/mutation-types'

  export default{
    data(){
      return {
        img_type: '',
      }
    },
    created: function () {
      document.title = this.$store.state.course.id == 0 ? '创建课程' : '修改课程';
      refresh_title();
    },
    computed: {
      // 使用对象展开运算符将此对象混入到外部对象中
      ...mapState({
        course: state => state.course,
        tag_str (state) {
          return state.course.tags.join()
        }
      })
    },
    methods: {
      dateinp: function (event) {
        if (event.target.value) {
          event.target.placeholder = event.target.value
        } else {
          event.target.placeholder = '请选择日期'
        }
      },
      save_tags: function () {
        var tags = []
        $('.right-tag input').each(function () {
          if ($(this).val()) {
            tags.push($(this).val());
          }
        });
        this.$store.state.course.advantage = $('#describe').val()
        this.$store.state.course.tags = tags
      },
      save_schedules: function () {
        var schedules = []
        if (this.course.type == 'red_on') {
          $('.right-plan section').each(function () {
            schedules.push({
              'date': $(this).find('.deadline').val(),
              'start': $(this).find('select').first().val(),
              'end': $(this).find('select').last().val(),
              'speaker': $(this).find(':text').val(),
              'intro': $(this).find('textarea').val()
            })
          });
        } else if (this.course.times > 5) {
          $('.right-plan section').each(function () {
            schedules.push({
              'date': $(this).find('.deadline').val(),
              'start': $(this).find('select').first().val(),
              'end': $(this).find('select').last().val(),
              'speaker': $(this).find(':text').val(),
              'intro': $(this).find('textarea').val()
            })
          });
        } else {
          $('.right-plan section').each(function () {
            schedules.push({
              'date': $(this).find('.deadline').val(),
              'am': {
                'start': $(this).find('.am select').first().val(),
                'end': $(this).find('.am select').last().val(),
                'speaker': $(this).find('.am :text').val(),
                'intro': $(this).find('.am textarea').val()
              },
              'pm': {
                'start': $(this).find('.pm select').first().val(),
                'end': $(this).find('.pm select').last().val(),
                'speaker': $(this).find('.pm :text').val(),
                'intro': $(this).find('.pm textarea').val()
              },
              'nt': {
                'start': $(this).find('.nt select').first().val(),
                'end': $(this).find('.nt select').last().val(),
                'speaker': $(this).find('.nt :text').val(),
                'intro': $(this).find('.nt textarea').val()
              }

            })
          });
        }

        this.$store.state.course.schedules = schedules
      },
      saveInfo: function () {
        if ($('#J-bright .unfold').length) {
          this.save_tags()
        }

        if ($('#J-schedules .unfold').length) {
          this.save_schedules()
        }
      },
      openModule: function (event) {
        $(event.currentTarget).next('.js-infoModule-middle').click()
      },
      toggleModule: function (event) {
        this.saveInfo()

        switchModule(event.target)
      },
      change_page: function (page) {
        this.saveInfo()
        this.$router.push({
          name: page,
          params: {courseType: this.$route.params.courseType}
        })

      },

      up_img: function (event, tpye) {
        var vm = this;
        vm.img_type = tpye;

        wx.chooseImage({
          count: 1,
          sizeType: ['compressed'],
          success: function (res) {
            upload(res.localIds);
          }
        });

        function upload(localIds) {
          var uploadImg = function (localId) {
            wx.uploadImage({
              localId: localId,
              isShowProgressTips: 1, // 默认为1，显示进度提示
              success: function (res) {
                $.post('/file/qiniu/wxup', {
                  'dir': 'course/' + vm.img_type + '/',
                  'media_id': res.serverId
                }, function (res) {
                  if (res.status == 1) {
                    if (vm.img_type == 'talker_pic') {
                      vm.course.talker_pic = res.up_path
                    } else if (vm.img_type == 'talker_qrcode') {
                      vm.course.talker_qrcode = res.up_path;

                    }
                    return res.up_path;
                  }

                })
              },
              fail: function (res) {
                alert(JSON.stringify(res));
                return false
              }
            });
          };

          uploadImg(localIds[0]);
        }
      },
    },
    filters: {
      timeLable: function (value) {
        return value == 'red_on' ? '次' : '天'
      }
    },
    beforeRouteEnter (to, from, next) {
      next(function (vm) {
        vm.$store.state.course.type = vm.$route.params.courseType
        window.scrollTo(0, 0);
      })
    }
  }
</script>
