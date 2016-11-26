<template>
  <div>
    <div id="container" v-show="address_show">
      <div class="createCourse-infoModule clearfix">
        <div class="infoModule-left infoModule-left-three" @click="openModule">
          <h1>往期集锦图片(9张)</h1>
        </div>
        <div class="js-infoModule-middle all-center" @click="toggleModule"></div>
        <div class="infoModule-right infoModule-right-three">
          <h1>往期集锦图片(9张)</h1>
          <div class="right-imgContainer img-delete-icon" @click="del_photo($event,'past_imgs')"
               v-for="p in course.past_imgs">
            <img :src="p | imgFile('!sq100')" alt="">
          </div>
          <div class="right-imgContainer add" @click="up_img($event,'past_imgs',9-course.past_imgs.length)"
               v-show="course.past_imgs.length<9">
          </div>
        </div>
      </div>

      <div class="createCourse-infoModule clearfix">
        <div class="infoModule-left infoModule-left-three" @click="openModule">
          <h1>关于学员照片(最多9张)</h1>
        </div>
        <div class="js-infoModule-middle all-center" @click="toggleModule"></div>
        <div class="infoModule-right infoModule-right-three">
          <h1>关于学员照片(最多9张)</h1>
          <div class="right-imgContainer img-delete-icon" @click="del_photo($event,'stu_imgs')"
               v-for="p in course.stu_imgs">
            <img :src="p | imgFile('!sq100')" alt="">
          </div>
          <div class="right-imgContainer add" @click="up_img($event,'stu_imgs',9-course.stu_imgs.length)"
               v-show="course.stu_imgs.length<9">
          </div>
        </div>
      </div>

      <div class="createCourse-infoModule clearfix" id="J-comments">
        <div class="infoModule-left infoModule-left-three" @click="openModule">
          <h1>往期学员信息及评价</h1>
        </div>
        <div class="js-infoModule-middle all-center" @click="toggleModule"></div>
        <div class="infoModule-right infoModule-right-three">
          <h1>往期学员信息及评价</h1>
          <div class="right-student">
            <div class="student-unit" v-for="stu in course.comments">
              <aside @click="up_img($event,'comments',1)"><img :src="stu.img | imgFile('!sq100')" alt=""></aside>
              <section>
                <div>
                  <label>学员姓名</label>
                  <input type="text" name="name" :value="stu.name" placeholder="中英文都可" maxlength="15"/>
                </div>
                <div>
                  <label>学员信息</label>
                  <input type="text" name="intro" :value="stu.intro" placeholder="店名/城市(10字内)" maxlength="10"/>
                </div>
                <div class="intro-student-container">
                  <label>学员评价</label>
                  <textarea type="text" name="text" :value="stu.text" placeholder="30字以内"
                            rows="2" cols="16" maxlength="30"></textarea>
                </div>
                <div>
                  <label>微信号</label>
                  <input type="text" name="weixin" :value="stu.weixin" placeholder="输入微信号" maxlength="15"/>
                </div>
              </section>
            </div>

            <div class="student-unit" v-if="new_comment" id="J-new_comment">
              <aside @click="up_img($event,'comments',1)">
              </aside>
              <section>
                <div>
                  <label>学员姓名</label>
                  <input type="text" name="name" placeholder="中英文都可" maxlength="15"/>
                </div>
                <div>
                  <label>学员信息</label>
                  <input type="text" name="intro" placeholder="店名/城市(10字内)" maxlength="15"/>
                </div>
                <div class="intro-student-container">
                  <label>学员评价</label>
                  <textarea type="text" name="text" placeholder="30字以内" rows="2" cols="16" maxlength="30"></textarea>
                </div>
                <div>
                  <label>微信号</label>
                  <input type="text" name="weixin" placeholder="输入微信号" maxlength="15"/>
                </div>
              </section>
            </div>
          </div>
          <footer>
            <a href="javascript:;" class="btn btn-border" @click="add_comments">增加学员</a>
          </footer>
        </div>
      </div>

      <div class="createCourse-infoModule clearfix">
        <div class="infoModule-left infoModule-left-three" @click="openModule">
          <h1>招生咨询</h1>
          <div>
            <label>联系人</label>
            <p>{{course.linkman?course.linkman:'输入联系人姓名'}}</p>
          </div>
          <div>
            <label>咨询电话</label>
            <p>{{course.phone?course.phone:'招生联系电话'}}</p>
          </div>
          <div>
            <label>优惠活动</label>
            <p>{{course.benefit?course.benefit:'15字以内概括优惠活动'}}</p>
          </div>
          <div>
            <label>微信号</label>
            <p>{{course.wxnum?course.wxnum:'暂无内容,点击输入'}}</p>
          </div>
          <div>
            <label>微信二维码</label>
            <p>{{course.wx_qrcode?'':'暂无内容,点击输入'}}</p>
            <div class="qrCode" v-if="course.wx_qrcode">
              <img :src="course.wx_qrcode | imgFile('!sq100')" alt="微信二维码">
            </div>
          </div>
        </div>
        <div class="js-infoModule-middle all-center" @click="toggleModule"></div>
        <div class="infoModule-right infoModule-right-three">
          <h1>招生咨询</h1>
          <div>
            <label for="linkman">联系人</label>
            <input id="linkman" type="text" v-model="course.linkman" placeholder="联系人姓名" maxlength="15"/>
          </div>
          <div>
            <label for="tel">咨询电话</label>
            <input id="tel" type="text" v-model="course.phone" placeholder="招生联系电话" maxlength="15"/>
          </div>
          <div>
            <label for="activity">优惠活动</label>
            <input id="activity" type="text" v-model="course.benefit" placeholder="15字以内概括优惠活动" maxlength="15"/>
          </div>
          <div>
            <label for="wx">微信号</label>
            <input id="wx" type="text" v-model="course.wxnum" placeholder="输入联系人微信号" maxlength="15"/>
          </div>

          <div>
            <label>微信二维码</label>
            <div class="qrCode-upload-border" @click="up_img($event,'wx_qrcode',1)">
              <!--<img src="../img/6-photo1.jpg" alt="">-->
              <img :src="course.wx_qrcode | imgFile('!sq100')" v-show="course.wx_qrcode">
            </div>
            <p class="p-center">点击上传微信二维码</p>
          </div>


        </div>
      </div>

      <div class="createCourse-infoModule clearfix" v-if="course.type!='red_on'">
        <div class="infoModule-left" @click="openModule">
          <h1>交通食宿</h1>
          <div>
            <label>详细地址</label>
            <p>{{course.detail_address?course.detail_address:'暂无内容,点击输入'}}</p>
          </div>
          <div>
            <label>交通推荐</label>
            <p>{{course.traffic?course.traffic:'暂无内容,点击输入'}}</p>
          </div>
          <div>
            <label>{{live_status?'包含住宿费':'不包含住宿费'}}</label>
          </div>
          <div>
            <label>{{eat_status?'包含餐饮费用':'不包含餐饮费用'}}</label>
          </div>
        </div>

        <div class="js-infoModule-middle all-center" @click="toggleModule"></div>

        <div class="infoModule-right">
          <h1>交通食宿</h1>
          <div>
            <label for="address">详细地址</label>
            <input type="hidden" v-model="course.lng">
            <input type="hidden" v-model="course.lat">
            <a href="javascript:;" v-on:click="myMapInfoShow" class="address-icon address-pos"></a>
            <input id="address" class="input-wide" type="text" placeholder="暂无内容,点击输入" v-model="course.detail_address"
                   maxlength="15"/>
          </div>
          <div>
            <label for="traffic">交通推荐</label>
            <input id="traffic" type="text" placeholder="暂无内容,点击输入" v-model="course.traffic" maxlength="15"/>
          </div>
          <div class="right-flex">
            <span class="right-cost" @click="liveFee"><i :class="{'selected':live_status}"></i>包含住宿费用</span>
            <span class="right-cost" @click="eatFee"><i :class="{'selected':eat_status}"></i>包含餐饮费用</span>
          </div>
        </div>
      </div>

      <div class="createCourse-btns">
        <a class="btn btn-border" @click="change_page('courseEdit2')">上一页</a>
        <a class="btn btn-border" @click="saveCourse">保存课程</a>
      </div>
    </div>
    <div class="choose-address-container" v-show="map_show">
      <div id="map_info" class="map" v-show="map_show">
      </div>
      <div class="map-message-container" v-show="map_show">
        <p class="title">位置</p>
        <p class="address-message">{{course.detail_address}}</p>
        <a href="javascript:;" class="map-btn" v-on:click="closeMap">确定</a>
      </div>
    </div>
  </div>
</template>

<script>
  import {mapState} from 'vuex'
  import * as types from '../../stores/edu/mutation-types'

  export default{
    data(){
      return {
        photo_length: 9,
        new_comment: this.$store.state.course.comments.length ? 0 : 1,
        eat_status: this.$store.state.course.canyin == 1 ? true : false,
        live_status: this.$store.state.course.shisu == 1 ? true : false,
        map_show: false,
        address_show: true,
        draw_map: 0,
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
        img_domain: state => state.img_domain,
        taglen (state) {
          return state.course.tags.length
        }
      })
    },
    methods: {
      liveFee: function () {
        this.live_status = !this.live_status
        this.$store.state.course.shisu = (this.live_status ? 1 : 0)
      },
      eatFee: function () {
        this.eat_status = !this.eat_status
        this.$store.state.course.canyin = (this.eat_status ? 1 : 0)
      },
      up_img: function (event, tpye, img_count) {
        var vm = this;
        vm.img_type = tpye;
        console.log(tpye + '::img_count::' + img_count);
        wx.chooseImage({
          count: img_count,
          sizeType: ['compressed'],
          success: function (res) {
            upload(res.localIds);
          }
        });

        function upload(localIds) {
          localIds = localIds.reverse()
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
                    if (vm.img_type == 'wx_qrcode') {
                      vm.course.wx_qrcode = res.up_path

                    } else if (vm.img_type == 'past_imgs') {
                      if (vm.course.past_imgs.length < 9) {
                        vm.course.past_imgs.push(res.up_path);
                      }

                    } else if (vm.img_type == 'stu_imgs') {
                      if (vm.course.stu_imgs.length < 9) {
                        vm.course.stu_imgs.push(res.up_path);
                      }

                    } else if (vm.img_type == 'comments') {
                      if (event.target.tagName == 'IMG') {
                        $(event.target).attr('src', vm.img_domain + res.up_path + '!sq100')

                      } else {
                        $(event.target).html($('<img>', {
                          'src': vm.$store.state.img_domain + res.up_path + '!sq100'
                        }));
                      }

                    }

                    if (localIds.length) {
                      uploadImg(localIds.pop());
                    }

                  }

                })
              },
              fail: function (res) {
                alert(JSON.stringify(res));
                return false
              }
            });
          };

          uploadImg(localIds.pop());
        }
      },
      del_photo: function (event, type) {
        if (type == 'stu_imgs') {
          var ss = this.course.stu_imgs.indexOf($(event.target).attr('src').replace(this.img_domain, '').replace('!sq100', ''))
          this.course.stu_imgs.splice(ss, 1)
        } else {
          var ss = this.course.past_imgs.indexOf($(event.target).attr('src').replace(this.img_domain, '').replace('!sq100', ''))
          this.course.past_imgs.splice(ss, 1)
        }

      },
      save_comments: function () {
        var comments = [];
        var vm = this;
        $('.right-student .student-unit').each(function () {
          if ($.trim($(this).find("input[name='name']").val())) {
            comments.push({
              'img': $(this).find('img').attr('src') ? $(this).find('img').attr('src').replace(vm.img_domain, '').replace('!sq100', '') : '',
              'name': $(this).find("input[name='name']").val(),
              'intro': $(this).find("input[name='intro']").val(),
              'text': $(this).find("textarea[name='text']").val(),
              'weixin': $(this).find("input[name='weixin']").val()
            })
          }

        });

        this.$store.state.course.comments = comments;
      },
      add_comments: function () {
        this.save_comments()
        $('#J-new_comment :text').val('');
        $('#J-new_comment textarea').val('');
        $('#J-new_comment img').attr('src', '');
        this.new_comment = 1
      },
      openModule: function (event) {
        $(event.currentTarget).next('.js-infoModule-middle').click()
      },
      toggleModule: function (event) {
        if ($('#J-comments .unfold').length) {
          this.save_comments()
          this.new_comment = 0
        }
        switchModule(event.target)
      },
      change_page: function (page) {
        if ($('#J-comments .unfold').length) {
          this.save_comments()
          this.new_comment = 0
        }

        this.$router.push({name: page, params: {courseType: this.$route.params.courseType}})
      },
      saveCourse: function () {
        var vm = this
        var info = {
          id: this.course.id,
          type: vm.$store.state.course.type,

          title: vm.$store.state.course.title,
          subtitle: vm.$store.state.course.subtitle,

          enroll_target: vm.$store.state.course.enroll_target,
          enroll_count: vm.$store.state.course.enroll_count,
          rest_count: vm.$store.state.course.rest_count,
          enroll_time: vm.$store.state.course.enroll_time,

          price: vm.$store.state.course.price,
          times: vm.$store.state.course.times,
          place: vm.$store.state.course.place,
          remark: vm.$store.state.course.remark,

          talker_pic: vm.$store.state.course.talker_pic,
          talker_name: vm.$store.state.course.talker_name,
          talker_skill: vm.$store.state.course.talker_skill,
          stu_count: vm.$store.state.course.stu_count,
          talker_intro: vm.$store.state.course.talker_intro,

          talker_title: vm.$store.state.course.talker_title,

          fans_count: vm.$store.state.course.fans_count,
          class_count: vm.$store.state.course.class_count,
          talker_qrcode: vm.$store.state.course.talker_qrcode,

          advantage: vm.$store.state.course.advantage,
          tags: JSON.stringify(vm.$store.state.course.tags),

          schedules: JSON.stringify(vm.$store.state.course.schedules),

          past_imgs: JSON.stringify(vm.$store.state.course.past_imgs),
          stu_imgs: JSON.stringify(vm.$store.state.course.stu_imgs),
          comments: JSON.stringify(vm.$store.state.course.comments),

          linkman: vm.$store.state.course.linkman,
          phone: vm.$store.state.course.phone,
          benefit: vm.$store.state.course.benefit,
          wxnum: vm.$store.state.course.wxnum,
          wx_qrcode: vm.$store.state.course.wx_qrcode,

          shisu: vm.$store.state.course.shisu,
          canyin: vm.$store.state.course.canyin,
          detail_address: vm.$store.state.course.detail_address,
          traffic: vm.$store.state.course.traffic,
          lng: vm.$store.state.course.lng,
          lat: vm.$store.state.course.lat
        };

        console.log('保存课程信息：：：')
        console.log(info)

        $.post('/course/add', info, function (res) {
          if (res.status == 1) {
//            vm.$store.commit(types.INIT_COURSE)
            vm.$router.push('/courses')
          }
        }, 'json');
      },
      myMapInfoShow: function () {
        var vm = this;
        if (vm.draw_map == 0) {
          var map = new BMap.Map("map_info");          // 创建地图实例
          if (vm.$store.state.course.lng && vm.$store.state.course.lat) {
            var point = new BMap.Point(vm.$store.state.course.lng, vm.$store.state.course.lat);  // 创建点坐标
            map.centerAndZoom(point, 15);                 // 初始化地图，设置中心点坐标和地图级别
            var geoc = new BMap.Geocoder();
            var mk = new BMap.Marker(point);
            map.addOverlay(mk);
            map.panTo(point);
            geocLocation(geoc, point)
            mk.enableDragging();//可拖拽
            mk.setAnimation(BMAP_ANIMATION_BOUNCE); //跳动的动画
            mk.addEventListener("dragend", function (e) {
              geocLocation(geoc, e.point)
            });
            map.addEventListener("click", function (e) {
              map.removeOverlay(mk);
              mk = new BMap.Marker(e.point);
              map.addOverlay(mk);
              map.panTo(e.point);
              mk.enableDragging();//可拖拽
              mk.addEventListener("dragend", function (e) {
                geocLocation(geoc, e.point);
              });
              geocLocation(geoc, e.point);

            })

          } else {
            var point = new BMap.Point(116.404, 39.915);  // 创建点坐标
            map.centerAndZoom(point, 15);                 // 初始化地图，设置中心点坐标和地图级别
            var geolocation = new BMap.Geolocation();
            var geoc = new BMap.Geocoder();
            geolocation.getCurrentPosition(function (r) {
              if (this.getStatus() == BMAP_STATUS_SUCCESS) {
                var mk = new BMap.Marker(r.point);
                map.addOverlay(mk);
                map.panTo(r.point);
                geocLocation(geoc, r.point)
                mk.enableDragging();//可拖拽
                mk.setAnimation(BMAP_ANIMATION_BOUNCE); //跳动的动画
                mk.addEventListener("dragend", function (e) {
                  geocLocation(geoc, e.point)
                });
                map.addEventListener("click", function (e) {
                  map.removeOverlay(mk);
                  mk = new BMap.Marker(e.point);
                  map.addOverlay(mk);
                  map.panTo(e.point);
                  mk.enableDragging();//可拖拽
                  mk.addEventListener("dragend", function (e) {
                    geocLocation(geoc, e.point);
                  });
                  geocLocation(geoc, e.point);

                })
              } else {
                alert('failed' + this.getStatus());
              }
            }, {enableHighAccuracy: true});
          }
          function geocLocation(geoc, pt) {
            geoc.getLocation(pt, function (rs) {
              var addComp = rs.addressComponents;
              vm.$store.state.course.detail_address = addComp.province + addComp.city + addComp.district + addComp.street + addComp.streetNumber
              vm.$store.state.course.lng = pt.lng;
              vm.$store.state.course.lat = pt.lat;
            });
          }
        }
        vm.draw_map = 1;
        vm.map_show = true;
        vm.address_show = false;
      },
      closeMap: function () {
        this.map_show = false;
        this.address_show = true;
      }
    },
    beforeRouteEnter (to, from, next) {
      next(function (vm) {
        console.log('vm.$store.state.img_domain')
        console.log(vm.$store.state.img_domain)
        vm.$store.state.course.type = vm.$route.params.courseType
        window.scrollTo(0, 0);
      })
    }
  }
</script>
