<template>
  <div id="tip-root" :style="hidden ? 'transform: translate(-500px,0px);' : ''">
    <div id="tip-info" :style="(isBad ? 'border-left: 6px solid #ff00fe !important;' : '')">
      <h1>{{text}}</h1>
      
    </div>
  </div>
</template>

<script>
export default {
  name: "tipbox",
  props: ["hidden", "text", 'isBad'],
  data() {
    return {};
  }
};
</script>

<style scoped>
#tip-root {
  position: fixed;
  left: 0;
  top: 0;
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  align-items: center;
  width: 400px;
  max-width: calc(100vw - 40px);
  height: 3rem;
  background-color: white;
  margin-top: 81vh;
  margin-left: 20px;

  z-index: 1000000;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
  /* background: #fff; */
  transition-property: transform;
  transition-duration: .5s;
  /* font-family: 'Roboto Mono', monospace; */
  font-family: "IBM Plex Mono", monospace;
  background-color: #161616;
  color: #f4f4f4;
}

#feed {
  height: calc(100% - 3rem);
  width: 400px;
  max-width: calc(100vw - 40px);
  object-fit: cover;
}

#tip-info {
  height: 3rem;
  width: 100%;
  display: flex;

  font-size: 1.5rem;
  border-left: 6px solid #95dfcc;
  padding-left: 10px;
  vertical-align: middle;

  align-items: center;
  /* text-align: right; */
}

#tip-info > h1 {
  height: 3rem;
  width: 100%;
  font-size: 1.5rem;
}

#tip-info > img {
  filter: invert(1);
  height: 100%;
  width: 50px;
  object-fit: cover;
}
</style>