<template>
  <div id="container" class="choose-address-container">
    <div class="map-message-container all-center" v-show="address_show">
      <p class="address">{{address}}</p>
      <a href="javascript:;" class="map-btn" v-on:click="myMapInfoShow">确定</a>
    </div>
      <div id="map_info" class="map" v-show="map_show">
      </div>
      <div class="map-message-container" v-show="map_show">
        <p class="title">位置</p>
        <p class="address">{{address}}</p>
        <a href="javascript:;" class="map-btn">确定</a>
      </div>
  </div>
</template>
<script>
  export default{
    data(){
      return {
        address: "",
        map_show: false,
        address_show: true
      }
    },
    created: function () {
      document.title = '地址选择';
      refresh_title();
    },
    methods: {
      myMapInfoShow: function () {
        console.log(11111)
        var vm = this;
        var map = new BMap.Map("map_info");          // 创建地图实例
        if (vm.lng && vm.lat) {
          var point = new BMap.Point(vm.lng, vm.lat);  // 创建点坐标
          map.centerAndZoom(point, 15);                 // 初始化地图，设置中心点坐标和地图级别
          var geoc = new BMap.Geocoder();
          var mk = new BMap.Marker(point);
          map.addOverlay(mk);
          map.panTo(point);
          geocLocation(geoc, point)
          mk.enableDragging();//可拖拽
          mk.setAnimation(BMAP_ANIMATION_BOUNCE); //跳动的动画
          mk.addEventListener("dragend", function (e) {
            geocLocation(geoc, e.point)
          });
          map.addEventListener("click", function (e) {
            map.removeOverlay(mk);
            mk = new BMap.Marker(e.point);
            map.addOverlay(mk);
            map.panTo(e.point);
            mk.enableDragging();//可拖拽
            mk.addEventListener("dragend", function (e) {
              geocLocation(geoc, e.point);
            });
            geocLocation(geoc, e.point);

          })

        } else {
          var point = new BMap.Point(116.404, 39.915);  // 创建点坐标
          map.centerAndZoom(point, 15);                 // 初始化地图，设置中心点坐标和地图级别
          var geolocation = new BMap.Geolocation();
          var geoc = new BMap.Geocoder();
          geolocation.getCurrentPosition(function (r) {
            if (this.getStatus() == BMAP_STATUS_SUCCESS) {
              var mk = new BMap.Marker(r.point);
              map.addOverlay(mk);
              map.panTo(r.point);
             geocLocation(geoc, r.point)
              mk.enableDragging();//可拖拽
              mk.setAnimation(BMAP_ANIMATION_BOUNCE); //跳动的动画
              mk.addEventListener("dragend", function (e) {
                    geocLocation(geoc, e.point)
              });
              map.addEventListener("click", function (e) {
                map.removeOverlay(mk);
                mk = new BMap.Marker(e.point);
                map.addOverlay(mk);
                map.panTo(e.point);
                mk.enableDragging();//可拖拽
                mk.addEventListener("dragend", function (e) {
                  geocLocation(geoc, e.point);
                });
                geocLocation(geoc, e.point);

              })
            } else {
              alert('failed' + this.getStatus());
            }
          }, {enableHighAccuracy: true});
        }
        function geocLocation(geoc, pt) {
          geoc.getLocation(pt, function (rs) {
            var addComp = rs.addressComponents;
            vm.address = addComp.province  + addComp.city  + addComp.district  + addComp.street +  addComp.streetNumber
            vm.lng = pt.lng;
            vm.lat = pt.lat;
          });
        }
        vm.map_show = true;
        vm.address_show = false;
      }
    },
    beforeRouteEnter (to, from, next) {
      next(function (vm) {
        vm.lng = vm.$route.query.lng;
        vm.lat = vm.$route.query.lat;
      })
    }
  }
</script>
