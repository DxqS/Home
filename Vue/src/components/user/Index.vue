<template>
  <div id="container">
    <div class="userCenter-header">
      <div class="userHead horiz-center">
        <img :src="avatar" class="head" alt="">
      </div>
      <div class="userName horiz-center">
        <p class="name">{{nickname}}</p>
        <p class="shopName" v-show="salon">{{salon}}</p>
      </div>
      <div class="userCenter-btn-container">
        <a href="javascript:;" class="userCenter-btn" @click="clickGray">
          <span class="userCenter-icon myTemplate"></span>
          <p class="template">历史或收藏</p>
        </a>
        <router-link :to="{path: '/pricing' }" class="userCenter-btn">
          <span class="vip no" v-show="level==1"></span>
          <span class="vip common" :class="days && days<4? 'red-circle':''" v-show="level==2"></span>
          <span class="vip" :class="days && days<4? 'red-circle': ''" v-show="level==3"></span>

          <p class="vip no" v-show="level==1">点击开通</p>
          <p class="vip common " v-show="level==2"></p>
          <p class="vip" v-show="level==3"></p>
          <p class="day" v-show="days && level!=1 && days>1">剩余{{days}}天</p>
          <p class="day" v-show="days && level!=1 && days<1">即将到期</p>
          <p class="day" v-show="!days && level!=1">已开通</p>
        </router-link>

        <a href="javascript:;" class="userCenter-btn" @click="clickGray">
          <span class="userCenter-icon Info"></span>
          <p class="myInfo">点击编辑</p>
        </a>
      </div>
      <span class="userCenter-icon" :class="sex==2?'woman':'man' "></span>
    </div>
    <nav class="userCenter-nav">
      <p class="p-margin-top">基础应用</p>
      <ul>
        <!--<li><a href="javascript:;" class=" userCenter-icon home off"></a></li>-->
        <li><a class=" userCenter-icon home off" @click="clickGray"></a></li>
        <!--<li><a href="javascript:;" class="userCenter-icon works off"></a></li>-->
        <li><a class="userCenter-icon works off" @click="clickGray"></a></li>
        <!--<li><a href="javascript:;" class="userCenter-icon post off"></a></li>-->
        <li><a class="userCenter-icon post off" @click="clickGray"></a></li>
      </ul>
    </nav>
    <nav class="userCenter-nav">
      <p class="p-vip">VIP高级应用</p>
      <ul>
        <li v-show="level!=3">
          <a class="userCenter-icon education" @click="vip_level"></a>
        </li>

        <li v-show="cert_status==0 && level==3">
          <router-link to="/cert/choice" class="userCenter-icon education"></router-link>
        </li>
        <li v-show="cert_status==3 && level==3">
          <router-link :to="{path:'/cert/'+partner}" class="userCenter-icon education"></router-link>
        </li>
        <li v-show="cert_status==1 && level==3">
          <a class="userCenter-icon education" @click="cert_wait"></a>
        </li>

        <li v-show="cert_status==2 && level==3">
          <a class="userCenter-icon education open" @click="edu_bar"></a>
          <span class="open-icon"></span>
        </li>

        <!--<li><a href="javascript:;" class="userCenter-icon live"></a></li>-->
        <!--<li><a href="javascript:;" class="userCenter-icon live open"></a></li>-->
        <li><a href="javascript:;" class="userCenter-icon live off" @click="clickGray"></a></li>
        <!--<li><a href="javascript:;" class="userCenter-icon salon"></a></li>-->
        <!--<li><a href="javascript:;" class="userCenter-icon salon open"></a></li>-->
        <li><a href="javascript:;" class="userCenter-icon salon off" @click="clickGray"></a></li>
        <!--<li><a href="javascript:;" class="userCenter-icon marketing off"></a></li>-->
        <li><a href="javascript:;" class="userCenter-icon marketing off" @click="clickGray"></a></li>
      </ul>
    </nav>

    <nav v-show="show_edu_bar" class="userCenter-second-nav">
      <ul>
        <li><a href="javascript:;" class="education-icon education-info" @click="edu('info')"></a></li>
        <li><a href="/wx/education#/courses" class="education-icon course"></a></li>
        <li><a href="javascript:;" class="education-icon courseTemplate" @click="edu('mine')"></a></li>
        <li><a href="javascript:;" class="education-icon templateShop" @click="edu('market')"></a></li>
      </ul>
      <a href="javascript:;" class="close" @click="edu_bar">关闭</a>
    </nav>

    <nav class="userCenter-nav nav-border-bottom">
      <p>其他服务</p>
      <ul>
        <!--<li><a href="javascript:;" class=" userCenter-icon kefu off"></a></li>-->
        <li><a class=" userCenter-icon kefu" @click="clickService"></a></li>
        <!--<li><a href="javascript:;" class="userCenter-icon course off"></a></li>-->
        <li><a class="userCenter-icon course off" @click="clickGray"></a></li>
      </ul>
    </nav>

    <div class="alert userCenter-alert" v-show="vip_no">
      <div class="cover"></div>
      <div class="popover all-center">
        <section>
          <p class="userCenter-alert-content-1">有疑问可直接通过公众号发送内容给我们，我们会尽快解决您的疑问</p>
        </section>
        <footer>
          <a href="javascript:;" class="btn" @click="closeWindow('vipNo')">我知道了</a>
        </footer>
      </div>
    </div>
    <div class="alert userCenter-alert" v-show="vip_service">
      <div class="cover"></div>
      <div class="popover all-center">
        <section>
          <p class="userCenter-alert-content">长按识别二维码添加客服，我们会解答您的疑问，并且可以收到最新模板上线通知哦，定期会有活动消息推送哦！</p>
        </section>
        <section>
          <a href="javascript:;" class="erweima-icon">
            <img :src="service_qrcode" alt="">
          </a>
          <a href="javascript:;" class=" zhiwenshibie-icon">
              <img src="/static/img/1-zhiwenshibie.png"/>
          </a>
        </section>
        <footer>
          <a href="javascript:;" class="btn" @click="closeWindow('vipService')">我知道了</a>
        </footer>
      </div>
    </div>
    <div class="alert" v-show="vip_limit">
      <div class="cover"></div>
      <div class="popover all-center">
        <section class="alert-content">
          <p>此功能需要开通VIP会员</p>
          <p>是否现在去开通</p>
        </section>
        <footer>
          <a href="javascript:;" class="btn btn-cancel" @click="closeWindow('vipLimit')">取消</a>
          <router-link to="/pricing" class="btn">确定</router-link>
        </footer>
      </div>
    </div>
    <div class="alert" v-show="gray_btn">
      <div class="cover"></div>
      <div class="popover all-center">
        <section class="alert-content">
          <p>此功能暂未开通，敬请期待</p>
        </section>
        <footer>
          <a href="javascript:;" class="btn" @click="closeWindow('grayBtn')">我知道了</a>
        </footer>
      </div>
    </div>

  </div>
</template>

<script>
  export default{
    data(){
      return {
        sex: 0,
        days: 0,
        level: 1,
        avatar: '',
        salon: '',
        nickname: '',
        cert_status: 0,
        show_edu_bar: false,
        vip_limit: false,
        vip_no: false,
        vip_service: false,
        service_qrcode: '',
        gray_btn: false,
        partner: ''
      }
    },
    created: function () {
      document.title = '个人中心';
      refresh_title();
    },
    computed: {
      vipclz(){
        if (this.level == 1) {
          return ''
        } else if (this.level == 2) {
          return 'common'
        } else if (this.level == 3) {
          return 'on'
        }
      }
    },
    methods: {
      edu_bar: function () {
        this.show_edu_bar = !this.show_edu_bar;
        return false;
      },
      edu: function (ss) {
        var vm = this;
        if (ss == 'info') {
          if (vm.role == 1) {
            vm.$router.push('/cert/organ/edit');
          } else {
            vm.$router.push('/cert/netred/edit');
          }
        } else {
          window.location.href = (vm.role == 1 ? '/wx/education#/temp/' + ss + '/5' : '/wx/education#/temp/' + ss + '/9');
        }
      },
      cert_wait: function () {
        if (this.role == 1) {
          this.$router.push('/cert/organ/info');
        } else {
          this.$router.push('/cert/netred/info');
        }
      },
      closeWindow: function (tt) {
        if (tt == 'vipLimit') {
          this.vip_limit = false;
        } else if (tt == 'vipNo') {
          this.vip_no = false;
        } else if (tt == 'vipService') {
          this.vip_service = false;
        } else {
          this.gray_btn = false;
        }
      },
      clickGray: function () {
        this.gray_btn = true
      },
      vip_level: function () {
        this.vip_limit = true;
      },
      clickService: function () {
        this.vip_no = this.level == 1 ? true : false
        this.vip_service = this.level != 1 ? true : false
      }
    },
    beforeRouteEnter(to, from, next)
    {
      next(function (vm) {
        $.post('/wx/user/info', function (res) {
          if (res.error_code == 20018) {
            window.location.href = '/wx/login';
            return false;
          }
          vm.salon = res.wxuser.salon
          vm.avatar = res.wxuser.headimgurl
          vm.nickname = res.wxuser.nickname
          vm.sex = res.wxuser.sex
          vm.days = res.wxuser.days
          vm.level = res.wxuser.level
          vm.cert_status = res.cert_status
          vm.partner = res.partner
          vm.role = res.role
          vm.service_qrcode = res.wxuser.level == 3 ? '/static/img/vip_service.jpg' : '/static/img/common_service.jpg'
        });

      })
    }
  }


</script>
