/**
 * Created by shenyufeng on 2016/11/18.
 */
import * as types from '../mutation-types'

// initial state
// shape: [{ id, quantity }]
const state = {
  id: 0,
  type: '',

  title: '',
  subtitle: '',

  enroll_target: '',
  enroll_count: '',
  rest_count: '',
  enroll_time: '',

  price: '',
  times: '',
  place: '',
  remark: '',

  talker_pic: '',
  talker_name: '',
  talker_skill: '',
  stu_count: '',
  talker_intro: '',

  talker_title: '',

  fans_count: '',
  class_count: '',
  talker_qrcode: '',

  advantage: '',
  tags: [],

  schedules: [],

  past_imgs: [],
  stu_imgs: [],
  comments: [],

  linkman: '',
  phone: '',
  benefit: '',
  wxnum: '',
  wx_qrcode: '',

  shisu: 0,
  canyin: 0,

  detail_address: '',
  traffic: '',
  lng:"",
  lat:""

}

// mutations
const mutations = {
  [types.INIT_COURSE] (state, course) {
    if (course) {

      state.id = course._id
      state.type = course.type

      state.title = course.info.title
      state.subtitle = course.info.subtitle

      state.enroll_target = course.info.enroll_target
      state.enroll_count = course.info.enroll_count
      state.rest_count = course.info.rest_count
      state.enroll_time = course.info.enroll_time

      state.price = course.info.price
      state.times = course.info.times
      state.place = course.info.place
      state.remark = course.info.remark

      state.talker_pic = course.talker.talker_pic
      state.talker_name = course.talker.talker_name
      state.talker_skill = course.talker.talker_skill
      state.stu_count = course.talker.stu_count
      state.talker_intro = course.talker.talker_intro

      state.talker_title = course.talker.talker_title

      state.fans_count = course.talker.fans_count
      state.class_count = course.talker.class_count
      state.talker_qrcode = course.talker.talker_qrcode

      state.advantage = course.bright.advantage
      state.tags = course.bright.tags

      state.schedules = course.schedules

      state.past_imgs = course.past_imgs
      state.stu_imgs = course.stu_imgs
      state.comments = course.comments

      state.linkman = course.contact.linkman
      state.phone = course.contact.phone
      state.benefit = course.contact.benefit
      state.wxnum = course.contact.wxnum
      state.wx_qrcode = course.contact.wx_qrcode

      state.shisu = course.contact.shisu
      state.canyin = course.contact.canyin

      state.detail_address = course.navigation.detail_address
      state.traffic = course.navigation.traffic
      state.lng = course.navigation.lng
      state.lat = course.navigation.lat

    } else {

      state.id = 0
      state.type = ''

      state.title = ''
      state.subtitle = ''

      state.enroll_target = ''
      state.enroll_count = ''
      state.rest_count = ''
      state.enroll_time = ''

      state.price = ''
      state.times = ''
      state.place = ''
      state.remark = ''

      state.talker_pic = ''
      state.talker_name = ''
      state.talker_skill = ''
      state.stu_count = ''
      state.talker_intro = ''

      state.talker_title = ''

      state.fans_count = ''
      state.class_count = ''
      state.talker_qrcode = ''

      state.advantage = ''
      state.tags = []

      state.schedules = []

      state.past_imgs = []
      state.stu_imgs = []
      state.comments = []

      state.linkman = ''
      state.phone = ''
      state.benefit = ''
      state.wxnum = ''
      state.wx_qrcode = ''

      state.shisu = 0
      state.canyin = 0

      state.detail_address = ''
      state.traffic = ''
      state.lng = ''
      state.lat = ''
    }
  }
}

export default {
  state,
  mutations
}
