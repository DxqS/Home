/**
 * Created by shenyufeng on 2016/11/9.
 */

import Vue from 'vue'
import VueRouter from 'vue-router'

import store from './stores/edu/index'

import CourseList from './components/edu/CourseList.vue'
import CoursePoster from './components/edu/CoursePoster.vue'
import CoursePosterList from './components/edu/CoursePosterList.vue'
import PosterDetail from './components/edu/PosterDetail.vue'

import EditCourse1 from './components/edu/EditCourse1.vue'
import EditCourse2 from './components/edu/EditCourse2.vue'
import EditCourse3 from './components/edu/EditCourse3.vue'

import ChoicePage from './components/edu/ChoicePage.vue'
import ChoicePoster from './components/edu/ChoicePoster.vue'
import HowCreateCourse from './components/edu/HowCreateCourse.vue'
import CourseShow from './components/edu/CourseShow.vue'
import CourseUsePosters from './components/edu/CourseUsePosters.vue'

import TempMarket from './components/edu/TempMarket.vue'
import TempMine from './components/edu/TempMine.vue'


Vue.use(VueRouter)

Vue.filter('time_format', function (value, input) {
  return $.myTime.UnixToDate(value, input == 'full')
})

Vue.filter('imgFile', function (value, fm) {
  if (!value) return ''
  return document.getElementById('app').dataset.img_domain + value + (fm ? fm : '')
})

const routes = [
  {path: '/', component: CourseList},

  {path: '/courses', component: CourseList},
  {path: '/courses/:courseId/poster/:num', component: CoursePosterList},
  {path: '/courses/:courseId/poster/detail/:posterId', component: CoursePoster},
  {path: '/courses/:courseId/mark/poster/detail/:posterId', component: PosterDetail},
  {path: '/courses/how/create/course', component: HowCreateCourse},
  {path: '/courses/show', component: CourseShow},
  {path: '/courses/:courseId/use/posters/:posterId', component: CourseUsePosters},

  {path: '/courses/edit/:courseType/e1', component: EditCourse1, name: 'courseEdit1'},
  {path: '/courses/edit/:courseType/e2', component: EditCourse2, name: 'courseEdit2'},
  {path: '/courses/edit/:courseType/e3', component: EditCourse3, name: 'courseEdit3'},

  {path: '/courses/:courseId/choice/page/:num', component: ChoicePage},
  {path: '/courses/:courseId/choice/poster/:num', component: ChoicePoster},

  {path: '/temp/market/:roleType', component: TempMarket},
  {path: '/temp/mine/:roleType', component: TempMine},

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
