<template>
  <div id="overlay-root" :style="hidden ? 'transform: translate(500px,0px);' : ''">
    <canvas id="map" />
    <h1 id="info">{{(markers+'').padStart(3, '0')}} responders nearby</h1>
  </div>
</template>

<script>
const scale = 5;
// const geometry = new THREE.BoxGeometry(1 * scale, 1 * scale, 50 * scale);
const geometry = new THREE.ConeGeometry( 5, 20, 3 ).rotateX(-Math.PI/2);

const prePassMaterial = new THREE.MeshStandardMaterial({
  color: "#ff00fe",
  opacity: 0.3,
  depthTest: false,
  transparent: true
});
const material = new THREE.MeshStandardMaterial({
  color: "#ff00fe",
  opacity: 0.9,
  transparent: true
});

function createCube() {
  const cube = new THREE.Object3D();

  const prePassMesh = new THREE.Mesh(geometry, prePassMaterial);
  prePassMesh.renderOrder = Number.MAX_SAFE_INTEGER - 1;
  cube.add(prePassMesh);

  const mesh = new THREE.Mesh(geometry, material);
  mesh.renderOrder = Number.MAX_SAFE_INTEGER;
  cube.add(mesh);
  return cube;
}

let map;
const options = {
  tilt: 50,
  // distance: 3000,
  distance: 700,
  center: new harp.GeoCoordinates(1.3455, 103.8361),
  angle: 50,
  markers: []
};

export default {
  name: "map-overlay",
  // beforeMount() {
  //   document.getElementById('overlay-root').style.transform = 'transform: translate(-500px,0px);'
  // },
  props: ["hidden", "lat", "lng"],
  data() {
    return {
      markers: 0,
    };
  },
  watch: {
    lat: function() {
      this.updateLocation();
    },
    lng: function() {
      this.updateLocation();
    }
  },
  methods: {
    updateLocation() {
      options.center = new harp.GeoCoordinates(this.lat, this.lng);
      for (let each of options.markers) {
        map.mapAnchors.remove(each);
      }
      options.markers = [];

      const count = Math.floor(Math.random()*3)+3;
      for (let i = 0; i < count; i++) {
        let marker = new harp.GeoCoordinates(this.lat+Math.random()*0.006-0.003, this.lng+Math.random()*0.006-0.003, 50);
        const cube = createCube();
        cube.geoPosition = marker;
        map.mapAnchors.add(cube);
        options.markers.push(cube);
      }

      map.update();
      this.markers = options.markers.length;
    }
  },
  mounted() {
    map = new harp.MapView({
      canvas: document.getElementById("map"),
      theme: "/3d-theme.json",
      maxVisibleDataSourceTiles: 40,
      tileCacheSize: 100
    });

    // const map = new harp.MapView({
    //   canvas: document.getElementById("3dmap"),
    //   theme: "//3d-theme.json",
    //   maxVisibleDataSourceTiles: 40,
    //   tileCacheSize: 100
    // });
    // const newSize = document.getElementById('3dmap-root').getBoundingClientRect();
    // map.resize(newSize.width, newSize.height);
    // window.onresize = () => {
    //   const newSize = document.getElementById('3dmap-root').getBoundingClientRect();
    //   map.resize(newSize.width, newSize.height);
    // }

    const omvDataSource = new harp.OmvDataSource({
      baseUrl: "https://xyz.api.here.com/tiles/herebase.02",
      apiFormat: harp.APIFormat.XYZOMV,
      styleSetName: "tilezen",
      authenticationCode: "AaEqtplvlWF4r0KXvrH-f5U"
    });
    map.addDataSource(omvDataSource);

    // const controls = new harp.MapControls(map);
    options.center = new harp.GeoCoordinates(this.lat, this.lng);
    map.addEventListener(harp.MapViewEventNames.Render, () => {
      map.lookAt(
        options.center,
        options.distance,
        options.tilt,
        (options.angle += 0.07)
      );
    });
    map.beginAnimation();
    // document.getElementById('overlay-root').style.transform = '';
    // this.hidden = false;
  }
};
</script>

<style scoped>
#overlay-root {
  position: fixed;
  right: 0;
  top: 0;
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  align-items: center;
  width: 400px;
  height: 60vh;
  background-color: white;
  margin-top: 20vh;
  margin-right: 20px;

  z-index: 1000000;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
  /* background: #fff; */
  transition-property: transform;
  transition-duration: 1s;
  /* font-family: 'Roboto Mono', monospace; */
  font-family: 'IBM Plex Mono', monospace;
  background-color: #161616;
  color: #f4f4f4;

}

#map {
  height: calc(100% - 3rem);
  width: 400px;
}

#info {
  height: 3rem;
  width: 100%;
  font-size: 1.5rem;
  border-left: 6px solid #95dfcc;
  padding-left: 10px;
  /* text-align: right; */
}
</style>