<template>
  <div>
    <div id="overlay-root" :style="(hidden ? 'transform: translate(-500px,0px);' : '')">
      <!-- 'cheene-ru-jPP4i-sirtA-unsplash.jpg-gray.jpg',
'lily-banse-2vcqwRL2xKk-unsplash.jpg-gray.jpg',
'lily-banse-C93HrzumjI0-unsplash.jpg-gray.jpg',
'lily-banse-H4UWdOd5vQM-unsplash-gray.jpg',
      'lily-banse-Rl6Xep37xS0-unsplash.jpg-gray.jpg',-->
      <img id="feed" :src="'images/'+images[Math.floor(seed) % images.length]" alt />
      <!-- <h1 id="info">camera feed</h1> -->
      <div id="info" :style="(isBad ? 'border-left: 6px solid #ff00fe !important;' : '')">
        <h1>camera feed</h1>
        <img :id="problem ==='blood' ? 'active' : 'inactive'" @mouseout="unhover()" @mouseover="hover('blood')" src="/icon/blood.svg" style="padding-bottom: 5px;" />
        <img :id="problem ==='crash' ? 'active' : 'inactive'" @mouseout="unhover()" @mouseover="hover('crash')" src="/icon/crash.svg" />
        <img :id="problem ==='fall' ? 'active' : 'inactive'" @mouseout="unhover()" @mouseover="hover('fall')" src="/icon/fall.svg" />
      </div>
    </div>
    <tipbox height="81vh" :hidden="!showTip" side="left" :isBad="onHover === problem">
      <h1>{{tipMsg}}</h1>
    </tipbox>
  </div>
</template>

<script>
import Tipbox from "./Tipbox";

const messages = {
  'blood': ['blood detector inactive', '*blood detector activated*'],
  'crash': ['crash detector inactive', '*crash detector activated*'],
  'fall': ['fall detector inactive', '*fall detector activated*'],
};

export default {
  name: "camera-feed",
  props: ["hidden", "seed", 'isBad'],
  components: {
    tipbox: Tipbox
  },
  watch: {
    seed() {
      console.log(this.seed);
      console.log(this.seed % this.images.length);
    },
    hidden() {
      if (this.hidden) this.showTip = false;
    },
    seed() {
      this.showTip = false;
      if (this.isBad) {
        
        this.problem = ['blood', 'crash', 'fall'][Math.floor(this.seed) % 3];
      } else {
        this.problem = 'none';
      }
    }
  },
  data() {
    return {
      index: 0,
      problem: '',
      images: [
        "cheene-ru-jPP4i-sirtA-unsplash.jpg-gray.jpg",
        "lily-banse-2vcqwRL2xKk-unsplash.jpg-gray.jpg",
        "lily-banse-C93HrzumjI0-unsplash.jpg-gray.jpg",
        "lily-banse-H4UWdOd5vQM-unsplash-gray.jpg",
        "lily-banse-Rl6Xep37xS0-unsplash.jpg-gray.jpg"
      ],
      showTip: false,
      tipMsg: '',
      onHover: '',
      nextState: false,
    };
  },
  methods: {
    hover(icon) {
      this.showTip = false;
      this.nextState = true;
      setTimeout(() => {
        if (this.hidden) return;
        this.showTip = this.nextState;
        this.tipMsg = messages[icon][icon === this.problem ? 1 : 0];
        this.onHover = icon;
      }, 500);
      
    },
    unhover(icon) {
      this.showTip = false;
      this.tipMsg = '';
      this.nextState = false;
    }
  }
};
</script>

<style scoped>
#overlay-root {
  position: fixed;
  left: 0;
  top: 0;
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  align-items: center;
  width: 400px;
  max-width: calc(100vw - 40px);
  height: 60vh;
  background-color: white;
  margin-top: 20vh;
  margin-left: 20px;

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

#info {
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

#info > h1 {
  height: 3rem;
  width: 100%;
  font-size: 1.5rem;
}

#info > img {
  filter: invert(1);
  height: 100%;
  width: 50px;
  object-fit: cover;
}

#active {
  filter: invert(20%) sepia(73%) saturate(3866%) hue-rotate(293deg) brightness(111%) contrast(133%) !important;
}
</style>