<template>
  <div id="root">
    <canvas id="map"/>
  </div>
</template>

<script>
export default {
  name: "map-overlay",
  mounted() {
    const map = new harp.MapView({
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

    const options = {
      tilt: 50,
      distance: 3000,
      center: new harp.GeoCoordinates(1.3455, 103.8361),
      angle: 50
    };

    map.addEventListener(harp.MapViewEventNames.Render, () => {
      map.lookAt(
        options.center,
        options.distance,
        options.tilt,
        (options.angle += 0.07)
      );
    });
    map.beginAnimation();
  }
};
</script>

<style scoped>
#root {
  position: fixed;
  right: 0;
  top: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 400px;
  height: 60vh;
  background-color: white;
  margin-top: 20vh;
  margin-right: 20px;

  z-index: 1000000;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
  /* background: #fff; */
}

#map {
  height: 100%;
  width: 400px;
}
</style>