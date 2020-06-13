<template>
  <div id="tip-root" :style="hidden ? 'transform: translate(500px,0px);' : ''">
    <div id="tip-info" :style="(isBad ? 'border-left: 6px solid #ff00fe !important;' : '')">
      <h1 id="label">call</h1>
      <div class="link">
        <a href="#">999</a>
      </div>
      <div class="link">
        <a href="#">995</a>
      </div>
      <div class="link">
        <a href="#">1777</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "callbox",
  props: ["hidden", 'isBad'],
  data() {
    return {};
  }
};
</script>

<style scoped>
#tip-root {
  position: fixed;
  right: 0;
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
  margin-right: 20px;

  z-index: 1000000;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
  /* background: #fff; */
  transition-property: transform;
  transition-duration: 1s;
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
  /* width: 100%; */
  font-size: 1.5rem;
}

#tip-info > img {
  filter: invert(1);
  height: 100%;
  width: 50px;
  object-fit: cover;
}

#label {
  margin-right: 80px;
}
.link {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  /* padding: 5px; */
  /* margin-left: 5px; */
  padding: 5px;
  padding-left: 15px;
  padding-right: 15px;
  justify-self: end;
  margin-left: auto;
  /* border-left: 2px solid #c6c6c6; */
  
  
}

.link > a {
  text-decoration: underline;
  color: #c6c6c6;
}

.link:hover {
  background-color: #2c2c2c;
  color: #f4f4f4;
}
</style>