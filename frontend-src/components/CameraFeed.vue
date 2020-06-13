<template>
  <div id="overlay-root" :style="hidden ? 'transform: translate(-500px,0px);' : ''">
    
<!-- 'cheene-ru-jPP4i-sirtA-unsplash.jpg-gray.jpg',
'lily-banse-2vcqwRL2xKk-unsplash.jpg-gray.jpg',
'lily-banse-C93HrzumjI0-unsplash.jpg-gray.jpg',
'lily-banse-H4UWdOd5vQM-unsplash-gray.jpg',
'lily-banse-Rl6Xep37xS0-unsplash.jpg-gray.jpg', -->
    <img id="feed" :src="'images/'+images[Math.floor(seed) % images.length]" alt="">
    <h1 id="info">camera feed</h1>
  </div>
</template>

<script>

export default {
  name: "camera-feed",
  props: ['hidden', 'seed'],
  watch: {
    seed() {
      console.log(this.seed);
      console.log(this.seed % this.images.length);
    
    }
  },
  data() {
    return {
      index: 0,
      images: ['cheene-ru-jPP4i-sirtA-unsplash.jpg-gray.jpg','lily-banse-2vcqwRL2xKk-unsplash.jpg-gray.jpg','lily-banse-C93HrzumjI0-unsplash.jpg-gray.jpg','lily-banse-H4UWdOd5vQM-unsplash-gray.jpg','lily-banse-Rl6Xep37xS0-unsplash.jpg-gray.jpg'],
    };
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
  font-family: 'IBM Plex Mono', monospace;
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
  font-size: 1.5rem;
  border-left: 6px solid #95dfcc;
  padding-left: 10px;
  vertical-align: middle;

  /* text-align: right; */
}
</style>