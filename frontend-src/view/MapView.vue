<template>
  <div>
    <div id="mapid"></div>
    <map-overlay :hidden="lastMarker.marker !== undefined ? false : true" :lat="lastMarker.marker !== undefined ? lastMarker.marker.getLatLng().lat : 0" :lng="lastMarker.marker !== undefined ? lastMarker.marker.getLatLng().lng : 0"/>
  </div>
</template>

<script>
import MapOverlay from '../components/MapOverlay';

const badMarkIcon = L.icon({
    iconUrl: '/bad-marker.png',
    shadowUrl: '/marker-shadow.png',
    iconSize:    [25, 41],
		iconAnchor:  [12, 41],
		popupAnchor: [1, -34],
		tooltipAnchor: [16, -28],
		shadowSize:  [41, 41]
});

const selectMarkIcon = L.icon({
    iconUrl: '/select-marker.png',
    shadowUrl: '/marker-shadow.png',
    iconSize:    [25, 41],
		iconAnchor:  [12, 41],
		popupAnchor: [1, -34],
		tooltipAnchor: [16, -28],
		shadowSize:  [41, 41]
});

export default {
  name: "map-view",
  data() {
    return {
      mymap: undefined,
      lastMarker: {},
    };
  },
  mounted() {
    
    this.mymap = L.map("mapid").setView([1.3455, 103.8361], 12);
    // L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    // L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png', {
    // L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png', {
    L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/dark-v8/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiZ2FyeS1raW0iLCJhIjoiY2syMGRjNTVxMTMwajNub2liODQ1OGs1ZCJ9.O631cR7G_-RlLGfIwXcCiA', {


      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(this.mymap);

    let carmeraCoords = [[1.275, 103.6213], [1.2964, 103.6284], [1.3189, 103.6385], [1.3388, 103.6466], [1.3212, 103.6639], [1.3306, 103.6752], [1.3212, 103.679], [1.3091, 103.679], [1.3194, 103.6876], [1.3282, 103.6876], [1.3394, 103.6915], [1.3486, 103.6939], [1.3714, 103.6895], [1.381, 103.6944], [1.3899, 103.6943], [1.4215, 103.6959], [1.4283, 103.7066], [1.4454, 103.7238], [1.3394, 103.7084], [1.2767, 103.7135], [1.3447, 103.7303], [1.3778, 103.7333], [1.4035, 103.7547], [1.4317, 103.7775], [1.3754, 103.7787], [1.3387, 103.7786], [1.3037, 103.772], [1.3006, 103.7945], [1.3316, 103.7985], [1.4325, 103.8004], [1.4583, 103.8222], [1.4348, 103.8258], [1.4089, 103.8294], [1.3781, 103.8282], [1.3328, 103.8177], [1.2949, 103.7983], [1.2652, 103.8196], [1.2517, 103.8229], [1.2889, 103.8282], [1.3212, 103.8254], [1.3675, 103.8481], [1.3987, 103.8567], [1.4013, 103.8841], [1.3723, 103.885], [1.36305, 103.88791], [1.3527, 103.8888], [1.3402, 103.8854], [1.32606, 103.88409], [1.3349, 103.909], [1.315, 103.9091], [1.3454, 103.9194], [1.3602, 103.9361], [1.369, 103.9382], [1.3666, 103.9609], [1.3472, 103.9631], [1.3204, 103.9562], [1.3327, 103.9703], [1.3587, 103.9856], [1.3908, 103.9876], [1.3406, 104.0077]];
    carmeraCoords = carmeraCoords.map(e => [e, Math.random()>0.8 ? true : false]);
    console.log(carmeraCoords);
    
    for (let each of carmeraCoords) {
      console.log(each);
      const [loc, isBad] = each;
      
      const marker = L.marker(loc, {
        icon: isBad ? badMarkIcon : new L.Icon.Default(),
      });
      
      marker.addTo(this.mymap);
      marker.on('click', function(e) {this.handleCameraClick(e, marker, isBad)}.bind(this));
    }
  },
  methods: {
    handleCameraClick(e,marker,isBad) {
      // const newCenter = {
      //   lat: e.latlng.lat,
      //   lng: e.latlng.lng,
      // };
      console.log(e);
      if (this.lastMarker.marker !== undefined) this.lastMarker.marker.setIcon(this.lastMarker.isBad ? badMarkIcon : new L.Icon.Default());
      marker.setIcon(selectMarkIcon)
      const center = this.mymap.latLngToLayerPoint(e.latlng).subtract(this.mymap.containerPointToLayerPoint(this.mymap.getSize()._divideBy(2)));
      this.mymap.panBy(center.subtract([-window.innerWidth/6,0]));
      
      this.$set(this.lastMarker, 'marker', marker);
      this.$set(this.lastMarker, 'isBad', isBad);
      // .subtract(L.containerPointToLayerPoint(L.getSize()._divideBy(2)))
      // mymap.panTo(e.latlng);
      // setTimeout(() => mymap.panBy([100,0]), 0.5);
      // console.log(e);

    },
  },
  mapInit() {
    console.log("hello");
  },
  components: {
    'map-overlay': MapOverlay,
  },
};
</script>

<style scoped>
#mapid {
  height: calc(100vh - 48px);
}
</style>