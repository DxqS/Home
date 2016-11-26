/**
 * Created by shenyufeng on 2016/11/9.
 */
/**
 * Created by shenyufeng on 2016/11/4.
 */
import Vue from 'vue'
import VueRouter from 'vue-router'

import store from './stores/user'

import Index from './components/user/Index.vue'
import Pricing from './components/user/Pricing.vue'
import CertChoice from './components/cert/Choice.vue'

import NetredCert from './components/cert/NetredCert.vue'
import NetredEdit from './components/cert/NetredEdit.vue'
import NetredInfo from './components/cert/NetredInfo.vue'
import OrganCert from './components/cert/OrganCert.vue'
import OrganEdit from './components/cert/OrganEdit.vue'
import OrganInfo from './components/cert/OrganInfo.vue'
import MapInfo from './components/cert/Map.vue'


Vue.use(VueRouter)

Vue.filter('time_format', function (value, input) {
  return $.myTime.UnixToDate(value, input == 'full')
})

Vue.filter('imgFile', function (value, fm) {
  if (!value) return ''
  return document.getElementById('app').dataset.img_domain + value + (fm ? fm : '')
})

const routes = [
  {path: '/', component: Index},
  {path: '/pricing', component: Pricing},
  {path: '/cert/choice', component: CertChoice},

  {path: '/cert/netred', component: NetredCert},
  {path: '/cert/netred/edit', component: NetredEdit},
  {path: '/cert/netred/info', component: NetredInfo},

  {path: '/cert/organ', component: OrganCert},
  {path: '/cert/organ/edit', component: OrganEdit},
  {path: '/cert/organ/info', component: OrganInfo},
  {path: '/cert/map/info', component: MapInfo},
]

const router = new VueRouter({
  routes
})

const app = new Vue({
  store,
  router
})

app.$mount('#app')

// Now the app has started!
