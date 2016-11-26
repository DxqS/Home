<template>
  <div id="container" class="vip-center-2">
    <h1>会员介绍对比</h1>
    <div class="table">
      <table border="0" cellspacing="0" cellpadding="0">
        <thead>
        <tr>
          <th></th>
          <th>
            <figure>
              <span class="logo vip-logo"></span>
              <figcaption>VIP会员</figcaption>
            </figure>
          </th>
          <th>
            <figure>
              <span class="logo simple-logo"></span>
              <figcaption>普通会员</figcaption>
            </figure>
          </th>
          <th>
            <figure>
              <span class="logo user-logo"></span>
              <figcaption>非会员</figcaption>
            </figure>
          </th>
        </tr>
        </thead>
        <tbody>
        <tr>
          <td class="t-title">基础功能</td>
          <td>
            <span class="logo-support support"></span>
          </td>
          <td>
            <span class="logo-support support"></span>
          </td>
          <td>
            <span>部分功能</span>
            <span class="addition">(除推广海报外)</span>
          </td>
        </tr>
        <tr class="padding">
          <td class="t-title">高级功能</td>
          <td>
            <span class="logo-support support"></span>
          </td>
          <td>
            <span class="logo-support unsupport"></span>
          </td>
          <td>
            <span class="logo-support unsupport"></span>
          </td>
        </tr>
        <tr>
          <td class="t-title">模版权限</td>
          <td>
            <span>所有模版</span>
            <span class="addition">(包括VIP专享)</span>
          </td>
          <td>
            <span>免费+</span>
            <span>会员模板</span>
          </td>
          <td>
            <span>免费模版</span>
          </td>
        </tr>
        <tr>
          <td class="t-title">客户服务</td>
          <td>
            <span class="list-item">VIP专属客服</span>
            <span class="list-item">VIP专属活动</span>
          </td>
          <td>
            <span class="list-item">会员客服</span>
            <span class="list-item">会员活动</span>
          </td>
          <td>
            <span>无</span>
          </td>
        </tr>
        <tr>
          <td class="t-title">会员福利</td>
          <td>
            <span>每月2次</span>
            <span>营销免费课程</span>
            <span class="addition">(全年24堂课)</span>
          </td>
          <td>
            <span>无</span>
          </td>
          <td>
            <span>无</span>
          </td>
        </tr>
        </tbody>
      </table>
      <div class="detail">
        <span class="detail-logo"></span>
        <p>普通会员升级VIP 时，未使用的普通会员期限
          按照实付价格折算成可支付金额，在购买VIP
          时抵扣掉。</p>
      </div>
    </div>
    <nav class="operate">
      <a @click="open_panel($event,'vip')" class="open-vip vip">
        {{vip_btn}}
      </a>
      <a @click="open_panel($event,'simple')" class="open-vip common" v-if="level<3">
        {{simple_btn}}
      </a>
    </nav>

    <!-- 点击开通，底部弹出窗口 -->
    <div class="pop-bg">
      <!-- 开通VIP会员 -->
      <div class="vip vs">
        <h2>{{vip_btn}} <i class="close" @click="close_panel"></i></h2>

        <template v-if="level==2">
          <div class="option">
            <input id="vip-upgrade" type="radio" name="vip" checked value="upgrade">
            <label for="vip-upgrade">升级支付{{pricing.upgrade}}元</label>
          </div>
        </template>
        <template v-else>
          <div class="option">
            <input id="vip-1" type="radio" name="vip" checked value="v1">
            <label for="vip-1">支付{{pricing.v1}}元/月</label>
          </div>
          <div class="option">
            <input id="vip-2" type="radio" name="vip" value="v3">
            <label for="vip-2" class="action" data-action="8.5折">支付{{pricing.v3}}元/季度</label>
          </div>
          <div class="option">
            <input id="vip-3" type="radio" name="vip" value="v12">
            <label for="vip-3" class="action" data-action="7.4折">支付{{pricing.v12}}元/年</label>
          </div>
        </template>

        <a @click="wxorder('vip')" class="submit">确定</a>
      </div>
      <!-- / 开通VIP会员 -->

      <!-- 开通普通会员 -->
      <div class="simple vs">
        <h2>{{simple_btn}} <i class="close" @click="close_panel"></i></h2>
        <div class="option">
          <input id="simple-1" type="radio" name="simple" checked value="m1">
          <label for="simple-1">支付{{pricing.m1}}元/月</label>
        </div>
        <div class="option">
          <input id="simple-2" type="radio" name="simple" value="m3">
          <label for="simple-2" class="action" data-action="9.5折">支付{{pricing.m3}}元/季度</label>
        </div>
        <div class="option">
          <input id="simple-3" type="radio" name="simple" value="m12">
          <label for="simple-3" class="action" data-action="8.5折">支付{{pricing.m12}}元/年</label>
        </div>
        <a @click="wxorder('simple')" class="submit">确定</a>
      </div>
      <!-- / 开通普通会员 -->

    </div>
    <!-- / 点击开通，底部弹出窗口 -->
  </div>
</template>

<script>
  export default{
    data(){
      return {
        avatar: '',
        nickname: '',
        sex: 0,
        level: 1,
        show_edu_bar: false,
        pricing: {}
      }
    },
    created: function () {
      document.title = true ? '会员中心' : '';
      refresh_title();
    },
    computed: {
      vip_btn(){
        if (this.level == 1) {
          return '开通VIP会员'
        } else if (this.level == 2) {
          return '升级VIP会员'
        } else if (this.level == 3) {
          return '续费VIP会员'
        }
      },
      simple_btn(){
        if (this.level == 1) {
          return '开通普通会员'
        } else if (this.level == 2) {
          return '续费普通会员'
        } else if (this.level == 3) {
          return '续费普通会员'
        }
      }
    },
    methods: {
      close_panel: function (event) {
        console.log('close_panel')
        $(event.target).parent().parent().animate({'bottom': '-5rem'}, 200, function () {
          $('.pop-bg').hide();
        });
        return false;
      },
      open_panel: function (event, mode) {
        $('.pop-bg').show();
        $('.pop-bg .' + mode).animate({
          'bottom': '0'
        }, 200);
        $('.pop-bg').bind("touchmove", function (e) {
          e.preventDefault();
        });
      },
      wxorder: function (mode) {
        var vm = this;
        var price = 0;
        var order_type = $('.pop-bg .' + mode).find('input:radio:checked').val();
        if (order_type == 'upgrade') {
          price = this.pricing.upgrade
        }
        $.post('/wx/order/create', {
          'order_type': order_type,
          'price': price
        }, function (res) {
          if (res.status == 1) {
            $.post("/wx/pay/order/" + res.order_id, function (res) {
              if (res.status == 1) {
                if (res.param) {
                  WeixinJSBridge.invoke('getBrandWCPayRequest', res.param, function (ret) {
                    if (ret.err_msg == "get_brand_wcpay_request:ok") {
                      vm.$router.push('/');
                    } else {
                      alert('微信支付失败');
                      return false;
                    }
                  }, 'json');
                }
              } else {
                alert('创建微信支付失败');
              }
            }, 'json');
          } else {
            alert('创建订单失败');
          }
        }, 'json');

      }
    },
    beforeRouteEnter (to, from, next) {
      next(function (vm) {
        $.post('/wx/order/pricing', function (ret) {
          vm.pricing = ret.pricing
          vm.level = ret.level
        })
      })
    }
  }
</script>
