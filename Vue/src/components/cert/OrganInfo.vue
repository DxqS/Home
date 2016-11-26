<template>
  <div id="container" class="request-sh request-org-nr">
    <!-- 提示 -->
    <div class="notification">
      <h2>{{status}}</h2>
    </div>

    <!-- 表单 -->
    <div class="form">
      <div class="manager-info">
        <h2>创办人信息</h2>
        <div class="form-control-item">
          <label for="manamger_name">创办人姓名：</label>
          <span id="manamger_name">{{founder_name}}</span>
        </div>
        <div class="form-control-item">
          <label for="manamger_mobile">创办人手机：</label>
          <span id="manamger_mobile">{{founder_mobile}}</span>
        </div>
        <div class="form-control-item">
          <label for="manamger_id">身份证号：</label>
          <span id="manamger_id">{{id_num}}</span>
        </div>
        <div class="form-control-item picture-container remove-padding">
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
      </div>
      <div class="organize-info">
        <h2 style="margin-top: .45rem;">教育机构信息</h2>
        <div class="form-control-item org-address-show">
          <label for="organize_name">机构名称：</label>
          <span id="organize_name">{{org_title}}</span>
        </div>
        <div class="form-control-item">
          <label for="organize_people">机构联系人：</label>
          <span id="organize_people">{{org_linkman}}</span>
        </div>
        <div class="form-control-item">
          <label for="organize_tel">联系电话：</label>
          <span id="organize_tel">{{org_phone}}</span>
        </div>
        <div class="form-control-item org-address-show">
          <label for="origanize_address">机构地址：</label>
          <span id="origanize_address">{{org_address}}</span>
        </div>
        <div class="form-control-item picture-container remove-padding">
          <label>LOGO图片：</label>
          <div class="pictures logo">
            <div class="erweima-item border-none" v-on:click="preview">
              <img :src="org_logo | imgFile('!sq150')" alt="机构LOGO">
            </div>
          </div>
        </div>
        <div class="form-control-item picture-container">
          <label>机构营业执照：</label>
          <div class="pictures zhizhao border-none">
            <div class="picture-item border-none" v-on:click="preview">
              <img :src="org_license | imgFile('!fw200')" alt="营业执照">
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
        status: '',
        founder_name: '',
        founder_mobile: '',
        id_num: '',
        id_front: '',
        id_back: '',
        org_title: '',
        org_linkman: '',
        org_phone: '',
        org_address: '',
        org_mobile: '',
        org_logo: '',
        org_license: ''
      }
    },
    created: function () {
      document.title = '认证信息';
      refresh_title();
    },
    methods: {
      preview: function (event) {
        var img = $(event.target);
        wx.previewImage({
          current: img.attr('src').replace('!fw200', '').replace('!sq150', ''),
          urls: [img.attr('src').replace('!fw200', '').replace('!sq150', '')]
        });
      }
    },
    beforeRouteEnter (to, from, next) {
      next(function (vm) {
        $.get('/organ/get', function (res) {
          if (res.status == 1) {
            vm.status = ["未付款...", "审核中...", "认证成功", "认证失败"][res.cert_status]
            vm.founder_name = res.founder_name
            vm.founder_mobile = res.founder_mobile
            vm.id_num = res.id_num
            vm.id_front = res.id_front
            vm.id_back = res.id_back
            vm.org_title = res.org_title
            vm.org_linkman = res.org_linkman
            vm.org_address = res.org_address
            vm.org_phone = res.org_phone
            vm.org_logo = res.org_logo
            vm.org_license = res.org_license
          }
          ;
          console.log(res);
        });
      })
    },
  }


</script>
