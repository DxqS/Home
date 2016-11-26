import Vue from 'vue'
import Vuex from 'vuex'
import * as actions from './actions'
import * as getters from './getters'
import course from './modules/course'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  actions,
  getters,
  modules: {
    course
  },
  state: {
    img_domain: document.getElementById('app').dataset.img_domain
  },
  strict: debug
})
