<template>
  <div class="edu-info">
    <h1>{{org_title}}</h1>
    <div class="form">
      <div class="form-control-item remove">
        <label for="manager">创办人：</label>
        <span id="manager" class="span-black">{{founder_name}}</span>
      </div>

      <div class="form-control-item">
        <label for="manager_name">创办人头衔：</label>
        <input id="manager_name" type="text" placeholder="例如：美业教育专家等(10字以内)" v-model="founder_title" maxlength="11">
      </div>
      <div class="form-control-item">
        <label for="honor" class="origanize-address-label">获得荣誉：</label>
        <textarea id="honor" type="text" class="origanize-address" placeholder="获得的业界称号等(60字以内)" v-model="honor"
                  maxlength="60"></textarea>
      </div>
      <div class="form-control-item create-header">
        <label>创始人头像：</label>
        <div class="erweima-item" @click="up_img($event,'avatar',1)">
          <img :src="founder_avatar | imgFile('!sq150')" alt="">
        </div>
        <p>点击上传创始人头像</p>
      </div>
      <div class="form-control-item">
        <label for="organize-intro" class="origanize-address-label">机构简介：</label>
        <textarea id="organize-intro" class="origanize-address" type="text" placeholder="简单介绍机构(80字以内)"
                  v-model="org_intro" maxlength="80"></textarea>
      </div>
      <div class="form-control-item environmental-photo-container">
        <label for="envPic">机构环境图片：</label>
        <span id="envPic">上传机构环境的相关照片(9张)</span>
        <div class="environmental-photo-container">

          <div class="environmental-photo-image" v-for="p in org_imgs">
            <img :src="p | imgFile('!sq150')" alt="">
          </div>

          <div class="environmental-photo-image add" @click="up_img($event,'org_imgs',9-org_imgs.length)"
               v-show="org_imgs.length<9">
          </div>

        </div>
      </div>
      <div class="form-submit form-submit-pos">
        <a v-on:click="save_info">保存</a>
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
  </div>
</template>

<script>
  export default{
    data(){
      return {
        org_title: '',
        founder_name: '',
        map_show: false,
        address_show: true,
        founder_title: '',
        founder_avatar: '',
        honor: '',
        org_intro: '',
        org_imgs: [],
        draw_map: 0,

        warn_info: false,
        detail_address: '点击定位详细地理位置',
        traffic: '',
      }
    },
    created: function () {
      document.title = '完善信息';
      refresh_title();
    },
    methods: {
      shutdown: function () {
        var vm = this;
        vm.warn_info = false;
        },
      save_info: function () {
        var vm = this;
        if (!(vm.founder_title && vm.honor && vm.org_intro && vm.org_imgs && vm.founder_avatar)){
          vm.warn_info = true;
          return false;
          }
        var cert = {
          founder_title: vm.founder_title,
          founder_avatar: vm.founder_avatar,
          honor: vm.honor,
          org_intro: vm.org_intro,
          org_imgs: vm.org_imgs.join(","),
        };
        $.post('/organ/edit', cert, function (res) {
          if (res.status == 1) {
            vm.$router.push('/');
          }
        }, 'json');
      },
      up_img: function (event, tpye, img_count) {
        var vm = this;
        vm.img_type = tpye;
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
                  'dir': 'cert/' + vm.img_type + '/',
                  'media_id': res.serverId
                }, function (res) {
                  if (res.status == 1) {
                    if (vm.img_type == 'org_imgs') {
                      if (vm.org_imgs.length < 9) {
                        vm.org_imgs.push(res.up_path);
                      }
                    }
                    if (vm.img_type == 'avatar') {
                      vm.founder_avatar = res.up_path;
                      return true;
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
    },

    beforeRouteEnter (to, from, next) {
      next(function (vm) {
        $.get('/organ/get', function (res) {
          if (res.status == 1) {
            vm.org_title = res.org_title;
            vm.founder_name = res.founder_name;
            vm.founder_avatar = res.founder_avatar;
            vm.founder_title = res.founder_title;
            vm.honor = res.honor;
            vm.org_intro = res.org_intro;
            vm.org_imgs = res.org_imgs ? res.org_imgs : [];
          }
        });
      })
    }
  }



</script>
