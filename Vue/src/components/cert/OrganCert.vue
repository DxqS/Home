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
      <div class="manager-info">
        <h2>创办人信息</h2>

        <div class="form-control-item">
          <label for="manamger_name">创办人姓名：</label>
          <input v-model="founder_name" id="manamger_name" type="text" placeholder="请输入真实姓名">
        </div>
        <div class="form-control-item">
          <label for="manamger_mobile">创办人手机：</label>
          <input v-model="founder_mobile" id="manamger_mobile" type="text" placeholder="请输入真实手机号码">
          <a @click="get_code" id="get-verification">发送验证码</a>
        </div>
        <div class="form-control-item">
          <label for="verification">输入验证码：</label>
          <input v-model="code" id="verification" type="text" placeholder="请输入收到的验证码">
        </div>

        <div class="form-control-item">
          <label for="manamger_id">身份证号：</label>
          <input id="manamger_id" v-model="id_num" type="text" placeholder="请输入身份证号">
        </div>
        <div class="form-control-item picture-container">
          <label for="manamger_picture">身份证照片：</label>
          <span id="manamger_picture">点击上传正反面证件照</span>
          <div class="pictures sfz">
            <div class="picture-item-container">
              <div class="picture-item" v-on:click="up_img($event,'front')">
                <img :src="id_front | imgFile('!fw200')" alt="身份证正面" v-show="id_front">
              </div>
              <span class="p-i-detail">正面</span>
            </div>
            <div class="picture-item-container">
              <div class="picture-item" v-on:click="up_img($event,'back')">
                <img :src="id_back | imgFile('!fw200')" alt="身份证反面" v-show="id_back">
              </div>
              <span class="p-i-detail">反面</span>
            </div>
          </div>
        </div>
      </div>

      <div class="organize-info">
        <h2>教育机构信息</h2>
        <div class="form-control-item">
          <label for="organize_name">机构名称：</label>
          <input v-model="org_title" id="organize_name" type="text" placeholder="请输入机构详细名称" maxlength="12">
        </div>
        <div class="form-control-item">
          <label for="organize_people">机构联系人：</label>
          <input v-model="org_linkman" id="organize_people" type="text" placeholder="请输入机构联系人姓名" maxlength="10">
        </div>
        <div class="form-control-item">
          <label for="organize_tel">联系电话：</label>
          <input v-model="org_phone" id="organize_tel" type="text" placeholder="请输入联系电话，手机，座机都可以" maxlength="15">
        </div>
        <div class="form-control-item">
          <label for="origanize_address" class="origanize-address-label">机构地址：</label>
          <textarea v-model="org_address" class="origanize-address" id="origanize_address" type="text"
                    placeholder="请输入机构的详细地址"></textarea>
        </div>
        <div class="form-control-item picture-container remove-padding">
          <label for="logo">LOGO图片：</label>
          <span id="logo">点击上传图片</span>
          <div class="pictures logo">
            <div class="erweima-item" v-on:click="up_img($event,'logo')">
              <img :src="org_logo | imgFile('!sq150')" alt="机构LOGO" v-show="org_logo">
            </div>
          </div>
        </div>
        <div class="form-control-item picture-container remove-padding">
          <label for="license">机构营业执照：</label>
          <span id="license">点击上传图片</span>
          <div class="pictures zhizhao">
            <div class="erweima-item" v-on:click="up_img($event,'license')">
              <img :src="org_license | imgFile('!sq150')" alt="营业执照" v-show="org_license">
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
        founder_name: '',
        founder_mobile: '',
        id_num: '',
        id_front: '',
        id_back: '',

        org_title: '',
        org_linkman: '',
        org_phone: '',
        org_address: '',

        org_logo: '',
        org_license: '',

        send_code: 0,
        img_type: '',
        order_no: 0,
        warn_info: false,
        error_text: "",
        error_show: false,
        status: 0,
      }
    },
    created: function () {
      document.title = '机构认证';
      refresh_title();
    },
    methods: {
      shutdown: function () {
        var vm = this;
        vm.warn_info = false;
        vm.error_show = false;
      },
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
          if (/^1[2|3|4|5|7|8]\d{9}$/.test(vm.founder_mobile)) {
            $.post('/auth/sendcode', {
              'phone': this.founder_mobile
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
          'order_type': 'c1'//机构
        }, function (res) {
          if (res.status == 1) {
            vm.order_no = res.order_no;
            $.post("/wx/pay/order/" + res.order_id, function (res) {
              if (res.status == 1) {
                if (res.param) {
                  WeixinJSBridge.invoke('getBrandWCPayRequest', res.param, function (ret) {
                    if (ret.err_msg == "get_brand_wcpay_request:ok") {
                      vm.$router.replace('/cert/organ/info');
                    } else {
                      vm.error_text = '微信支付失败';
                      vm.error_show = true;
                      return false;
                    }
                  }, 'json');
                }
              } else {
                vm.error_text = '创建微信支付失败';
                vm.error_show = true;
              }
            }, 'json');
          } else {
            vm.error_text = '创建订单失败';
            vm.error_show = true;
          }
        }, 'json');
      },

      save_cert: function () {
        var vm = this;
        var cert = {
          founder_name: vm.founder_name,
          founder_mobile: vm.founder_mobile,
          code: vm.code,

          id_num: vm.id_num,
          id_front: vm.id_front,
          id_back: vm.id_back,

          org_title: vm.org_title,
          org_linkman: vm.org_linkman,
          org_phone: vm.org_phone,
          org_address: vm.org_address,

          org_logo: vm.org_logo,
          org_license: vm.org_license,
        };
        if (!(vm.founder_name && vm.founder_mobile && vm.id_num && vm.id_front && vm.id_back
          && vm.org_title && vm.org_linkman && vm.org_phone && vm.org_address
          && vm.org_license && vm.org_logo && vm.code)) {
          vm.warn_info = true;
          return false;
        }
        if (vm.status == 3){
          $.post('/organ/cert', cert, function (res) {
          if (res.status == 1) {
              //认证失败后提交成功直接跳转
              vm.$router.replace('/cert/organ/info');
              return true;
          } else {
              vm.error_text = res.error_msg;
              vm.error_show = true;
            }
          }, 'json');
         } else {
          $.post('/organ/cert', cert, function (res) {
            if (res.status == 1) {
              vm.create_order();
              } else {
              vm.error_text = res.error_msg;
              vm.error_show = true;
                }
          } , 'json');
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
                  'dir': 'cert/organ/',
                  'media_id': res.serverId
                }, function (res) {
                  if (res.status == 1) {
                    if (vm.img_type == 'logo') {
                      vm.org_logo = res.up_path
                    }
                    else if (vm.img_type == 'license') {
                      vm.org_license = res.up_path;
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

    },
    beforeRouteEnter (to, from, next) {
      next(function (vm) {
        $.get('/organ/get', function (res) {
          if (res.status == 1) {
            vm.founder_name = res.founder_name;
            vm.founder_mobile = res.founder_mobile;
            vm.id_num = res.id_num;
            vm.id_front = res.id_front;
            vm.id_back = res.id_back;

            vm.org_title = res.org_title;
            vm.org_linkman = res.org_linkman;
            vm.org_phone = res.org_phone;
            vm.org_address = res.org_address;
            vm.org_logo = res.org_logo;
            vm.org_license = res.org_license;
            vm.status = res.cert_status;
          }
        });
      })
    }
  }
</script>
