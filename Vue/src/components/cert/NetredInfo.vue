<template>
  <div id="container" class="request-org-nr request-sh">
    <!-- 提示 -->
    <div class="notification">
      <h2>{{status}}</h2>
    </div>

    <!-- 表单 -->
    <div class="form">
      <div class="user-info">
        <h2>本人信息</h2>
        <div class="form-control-item">
          <label for="user_name">姓名：</label>
          <span id="user_name" type="text">{{name}}</span>
        </div>
        <div class="form-control-item">
          <label for="mobile">手机：</label>
          <span id="mobile" type="text">{{mobile}}</span>
        </div>
        <div class="form-control-item">
          <label for="verification">身份证号码：</label>
          <span id="verification" type="text">{{id_num}}</span>
        </div>
        <div class="form-control-item picture-container">
          <label>身份证照片：</label>
          <div class="pictures sfz">
            <div class="picture-item border-none" v-on:click="preview">
              <img :src="id_front | imgFile('!fw200')" alt="身份证正面">
            </div>
            <div class="picture-item border-none" v-on:click="preview">
              <img :src="id_back | imgFile('!fw200')" alt="身份证背面">
            </div>
          </div>
        </div>
        <div class="form-control-item picture-container">
          <label>正面五官照：</label>
          <div class="pictures wuguan">
            <div class="erweima-item border-none" v-on:click="preview">
              <img :src="face | imgFile('!sq150')" alt="五官正面照">
            </div>
          </div>
        </div>
        <div class="form-control-item picture-container">
          <label>微信二维码：</label>
          <div class="pictures twowm">
            <div class="erweima-item border-none" v-on:click="preview">
              <img :src="wx_qrcode | imgFile('!sq150')" alt="微信二维码">
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default{
    data(){
      return {
        status: 0,
        name: '',
        mobile: '',
        face: '',
        wx_qrcode: '',
        id_num: '',
        id_front: '',
        id_back: '',
        show_edu_bar: false
      }
    },
    created: function () {
      document.title = '认证信息';
      refresh_title();
    },
    beforeRouteEnter (to, from, next) {
      next(function (vm) {
        $.get('/net/get', function (res) {
          if (res.status == 1) {
            vm.status = ["未付款...", "审核中...", "认证成功", "认证失败"][res.cert_status];
            vm.name = res.name;
            vm.mobile = res.mobile;
            vm.face = res.face;
            vm.wx_qrcode = res.wx_qrcode;
            vm.id_num = res.id_num;
            vm.id_front = res.id_front;
            vm.id_back = res.id_back
          }
        });
      })
    },
    methods: {
      preview: function (event) {
        var img = $(event.target);
        wx.previewImage({
          current: img.attr('src').replace('!fw200', '').replace('!sq150', ''),
          urls: [img.attr('src').replace('!fw200', '').replace('!sq150', '')]
        });
      },
      edu_bar: function () {
        this.show_edu_bar = !this.show_edu_bar;
        return false;
      }
    },
  }
</script>
