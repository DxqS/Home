<template>
  <div id="container" class="edu-info">
    <div class="form">
      <div class="form-control-item upload-header">
        <label>头像照片：</label>
        <p>点击上传头像</p>
        <div v-on:click="up_img" class="erweima-item">
          <img :src="avatar | imgFile('!sq150')" alt="">
        </div>
      </div>
      <div class="form-control-item remove">
        <label for="manager">姓名：</label>
        <span id="manager" class="span-black">{{name}}</span>
      </div>
      <div class="form-control-item remove">
        <label for="mobile">手机号：</label>
        <span id="mobile" type="text" class="span-black">{{mobile}}</span>
      </div>
      <div class="form-control-item">
        <label for="wechat">微信号：</label>
        <input id="wechat" v-model="wx_id" type="text">
      </div>
      <div class="form-control-item">
        <label for="intro">个人精简介绍：</label>
        <input id="intro" v-model="brief" type="text" placeholder="例如：美业教育专家等(15字以内)" maxlength="15">
      </div>
      <div class="form-control-item">
        <label for="fans-nums">粉丝数量：</label>
        <input id="fans-nums" v-model="fan" type="number" min="0" placeholder="输入数字">
      </div>
      <div class="form-control-item">
        <label for="personal-intro">个人简介：</label>
        <input id="personal-intro" v-model="intro" type="text" placeholder="简单介绍你自己(40字以内)" maxlength="40">
      </div>
      <div class="form-control-item">
        <label for="strong-point">擅长技法：</label>
        <input id="strong-point" v-model="skill" type="text" placeholder="介绍自己擅长的剪发技术(10字以内)" maxlength="10">
      </div>
      <div class="form-submit form-submit-pos">
        <a @click="save_info">提交</a>
      </div>
    </div>
    <div v-show="warn_info" class="alert">
      <div class="cover"></div>
      <div class="popover all-center">
        <section class="alert-content">
          <p>您的信息尚未完善</p>
          <p>先去完善信息吧</p>
        </section>
        <footer>
          <a v-on:click="shutdown" class="btn btn-cancel">取消</a>
          <a v-on:click="shutdown" class="btn know">去完善</a>
        </footer>
      </div>
    </div>
    <div v-show="success_info" class="alert">
      <div class="cover"></div>
      <div class="popover all-center">
        <section class="alert-content">
          <p>上传成功</p>
        </section>
        <footer>
          <a v-on:click="shutdown" class="btn btn-cancel">我知道了</a>
          <a herf="/" class="btn know">回主页</a>
        </footer>
      </div>
    </div>
    <div v-show="error_show" class="alert">
      <div class="cover"></div>
      <div class="popover all-center">
        <section class="alert-content">
          <p>{{error_text}}</p>
        </section>
        <footer>
          <a v-on:click="shutdown" class="btn btn-cancel">取消</a>
          <a v-on:click="shutdown" class="btn know">我知道了</a>
        </footer>
      </div>
    </div>
  </div>

</template>

<script>
  export default{
    data(){
      return {
        name: '',
        mobile: '',
        avatar: '',
        wx_id: '',
        brief: '',
        intro: '',
        skill: '',
        fan: '',
        warn_info: false,
        error_show: false,
        error_text: '',
      }
    },
    created: function () {
      document.title = '完善信息';
      refresh_title();
    },
    methods: {
      shutdown: function () {
        var vm = this;
        this.warn_info = false;
      },
      save_info: function () {
        var vm = this;
        if (!(vm.avatar && vm.brief && vm.intro && vm.skill && vm.fan && vm.wx_id)) {
          vm.warn_info = true;
          return false;
        }
        var cert = {
          avatar: vm.avatar,
          brief: vm.brief,
          intro: vm.intro,
          skill: vm.skill,
          fan: vm.fan,
          wx_id: vm.wx_id,
        };
        $.post('/net/edit', cert, function (res) {
          if (res.status == 1) {
            vm.$router.push('/');
          }
        }, 'json');
      },
      up_img: function () {
        var vm = this;
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
                  'dir': 'cert/netred/',
                  'media_id': res.serverId
                }, function (res) {
                  if (res.status == 1) {
                    vm.avatar = res.up_path;
                    return res.up_path;
                  }
                })
              },
              fail: function (res) {
                vm.error_text = JSON.stringify(res);
                vm.error_show = true;
                return false;
              }
            });
          };

          uploadImg(localIds[0]);
        }
      },
    },
    beforeRouteEnter (to, from, next) {
      next(function (vm) {
        $.get('/net/get', function (res) {
          if (res) {
            vm.name = res.name;
            vm.mobile = res.mobile;
            vm.wx_id = res.wx_id;
            vm.avatar = res.avatar;
            vm.brief = res.brief;
            vm.intro = res.intro;
            vm.skill = res.skill;
            vm.fan = res.fan;
          }

        });
      })
    }
  }



</script>
