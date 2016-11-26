<template>
  <div id="container" class="request-org-nr">
    <!-- 提示 -->
    <div class="notification">
      <h2>认证须知</h2>
      <p>
        首次使用教育推广功能需要申请教育认证，支付认证费用并填写认证资料（必须保证填写内容的真实性，认证信息内容一经核实，不得更改），我们会根据您提供的资料进行审核。审核通过，您会拥有一年免费使用教育推广功能的权限，到期续年费可继续使用；审核未通过，我们会通过微信公众号发送消息通知，再次认证则无需付费，审核需要7个工作日，请耐心等待，不便之处请您谅解！ </p>
    </div>

    <!-- 表单 -->
    <div class="form">
      <div class="user-info">
        <h2>本人信息</h2>
        <div class="form-control-item">
          <label for="user_name">姓名：</label>
          <input id="user_name" v-model='name' type="text" placeholder="请输入真实姓名">
        </div>
        <div class="form-control-item">
          <label for="mobile">手机：</label>
          <input id="mobile" v-model="mobile" type="text" placeholder="请输入真实手机号码">
          <a v-on:click="get_code" id="get-verification">发送验证码</a>
        </div>
        <div class="form-control-item">
          <label for="verification">输入验证码：</label>
          <input id="verification" v-model="code" type="text">
        </div>
        <div class="form-control-item">
          <label for="_id">身份证号：</label>
          <input id="_id" v-model="id_num" type="text" placeholder="请输入您本人的身份证号">
        </div>
        <div class="form-control-item picture-container">
          <label for="id_picture">身份证照片：</label>
          <span id="id_picture">点击上传正反面证件照</span>
          <div class="pictures sfz">
            <div class="picture-item" v-on:click="up_img($event,'front')">
              <span class="p-i-detail">正面</span>
              <img :src="id_front | imgFile('!fw200')" alt="身份证正面" v-show="id_front">
            </div>
            <div class="picture-item" v-on:click="up_img($event,'back')">
              <span class="p-i-detail">反面</span>
              <img :src="id_back | imgFile('!fw200')" alt="身份证背面" v-show="id_back">
            </div>
          </div>
        </div>
        <div class="form-control-item picture-container remove-padding">
          <label for="user_picture">正面五官照：</label>
          <span id="user_picture" type="text">点击上传，要能看清五官</span>
          <div class="pictures wuguan">
            <div class="erweima-item" v-on:click="up_img($event,'face')">
              <img :src="face | imgFile('!sq150')" alt="五官正面照" v-show="face" class="cba">
            </div>
          </div>
        </div>
        <div class="form-control-item picture-container remove-padding">
          <label for="two_picture">微信二维码：</label>
          <span id="two_picture">点击上传您的微信二维码</span>
          <div class="pictures twowm">
            <div class="erweima-item" v-on:click="up_img($event,'wx_qrcode')">
              <img :src="wx_qrcode | imgFile('!sq150')" alt="微信二维码" v-show="wx_qrcode" class="abc">
            </div>
          </div>
        </div>
      </div>
      <div class="form-submit">
        <div class="form-bill">认证需支付：<span id="fill">379</span>元</div>
        <a v-on:click="save_cert">认证</a>
      </div>
    </div>
    <div v-show="warn_info" class="alert">
      <div class="cover"></div>
      <div class="popover all-center">
        <section class="alert-content">
          <p>您的认证信息尚未完善</p>
          <p>先去完善信息吧</p>
        </section>
        <footer>
          <a v-on:click="shutdown" class="btn btn-cancel">取消</a>
          <a v-on:click="shutdown" class="btn know">去完善</a>
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
        code: '',
        face: '',
        wx_qrcode: '',
        id_num: '',
        id_front: '',
        id_back: '',
        img_type: '',
        send_code: 0,
        warn_info: false,
        error_text: "",
        error_show: false,
        status: 0,
      }
    },
    created: function () {
      document.title = '网红认证';
      refresh_title();
    },
    beforeRouteEnter (to, from, next) {
      next(function (vm) {
        $.get('/net/get', function (res) {
          if (res) {
            vm.status = res.cert_status;
            vm.name = res.name;
            vm.mobile = res.mobile;
            vm.face = res.face;
            vm.wx_qrcode = res.wx_qrcode;
            vm.id_num = res.id_num;
            vm.id_front = res.id_front;
            vm.id_back = res.id_back;
          }
        });
      })
    },
    methods: {
      countDown: function (btn) {
        var vm = this;
        vm.send_code = 60;
        function time() {
          if (vm.send_code == 0) {
            btn.html("重新发送");
          } else {
            btn.html(vm.send_code + "秒后重发");
            vm.send_code--;
            setTimeout(function () {
              time();
            }, 1000);
          }
        }

        time();
      },

      get_code: function (event) {
        if (this.send_code == 0) {
          var vm = this;
          if (/^1[2|3|4|5|7|8]\d{9}$/.test(vm.mobile)) {
            $.post('/auth/sendcode', {
              'phone': this.mobile
            }, function (res) {
              if (res.status == 1) {
                vm.countDown($(event.target));
              }
            }, 'json');
          } else {
            vm.error_text = '请输入正确的手机号';
            vm.error_show = true;
            return false;
          }
        } else {
          return false;
        }
      },
      create_order: function () {
        var vm = this;
        $.post('/wx/order/create', {
          'order_type': 'c2'//网红
        }, function (res) {
          if (res.status == 1) {
            vm.order_no = res.order_no;
            $.post("/wx/pay/order/" + res.order_id, function (res) {
              if (res.status == 1) {
                if (res.param) {
                  WeixinJSBridge.invoke('getBrandWCPayRequest', res.param, function (ret) {
                    if (ret.err_msg == "get_brand_wcpay_request:ok") {
                      vm.$router.replace('/cert/netred/info');
                    } else {
                      vm.error_text = '微信支付失败';
                      vm.error_show = true;
                      return false;
                    }
                  }, 'json');
                }
              } else {
                vm.error_text = '创建微信支付失败：：' + vm.order_no;
                vm.error_show = true;
              }
            }, 'json');
          } else {
            vm.error_text = '创建订单失败';
            vm.error_show = true;
          }
        }, 'json');
      },
      shutdown: function () {
        this.warn_info = false;
        this.error_show = false;
      },
      save_cert: function () {
        var vm = this;

        if (!(this.name && this.face && this.mobile && this.code && this.id_num && this.id_front && this.id_back && this.wx_qrcode)) {
          this.warn_info = true;
          return false;
        }
        var cert = {
          name: this.name,
          face: this.face,
          mobile: this.mobile,
          code: this.code,
          id_num: this.id_num,
          id_front: this.id_front,
          id_back: this.id_back,
          wx_qrcode: this.wx_qrcode,
        };

        if (vm.status == 3) {
          $.post('/net/cert', cert, function (res) {
            if (res.status == 1) {
              //认证失败后提交成功直接跳转
              vm.$router.replace('/cert/netred/info');
              return true;
            } else {
              vm.error_text = res.error_msg;
              vm.error_show = true;
            }
          }, 'json');
        } else {
          $.post('/net/cert', cert, function (res) {
            if (res.status == 1) {
              vm.create_order();
            } else {
              vm.error_text = res.error_msg;
              vm.error_show = true;
            }
          }, 'json');
        }
      },
      up_img: function (event, type) {
        var vm = this;
        vm.img_type = type;

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
                  'dir': 'cert/netred/' + vm.img_type + '/',
                  'media_id': res.serverId
                }, function (res) {
                  if (res.status == 1) {
                    if (vm.img_type == 'face') {
                      vm.face = res.up_path
                    }
                    else if (vm.img_type == 'wx_qrcode') {
                      vm.wx_qrcode = res.up_path;
                    }
                    else if (vm.img_type == 'front') {
                      vm.id_front = res.up_path;
                    }
                    else if (vm.img_type == 'back') {
                      vm.id_back = res.up_path;
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
    }
  }


</script>
