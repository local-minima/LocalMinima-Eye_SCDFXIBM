<template>
  <div class="root">
    <div class="main-content">
      
      <api-endpoint url="https://scdfxibm2020.garykim.dev/pose/model/predict" sample1="/model/pose/non-blood.png"/>
      <api-endpoint url="https://scdfxibm2020.garykim.dev/fire" sample1="/model/fire/car-fire.jpg" sample2="/model/fire/no-fire.jpg"/>
      <api-endpoint url="https://scdfxibm2020.garykim.dev/traffic" sample1="/model/traffic/accident.jpg" sample2="/model/traffic/sparse-traffic.jpg"/>
      <api-endpoint url="https://scdfxibm2020.garykim.dev/body" sample1="/model/body/human.jpeg" sample2="/model/body/robin.jpg"/>
      <api-endpoint url="https://scdfxibm2020.garykim.dev/blood" sample1="/model/blood/non-blood.png" sample2="/model/blood/blood-demo.jpg"/>
      

    </div>
  </div>
</template>

<script>
import APIEndpoint from '../components/APIEndpoint';

export default {
  name: "APIView",
  computed: {},
  data() {
    return {
    };
  },
  mounted() {
  },
  components: {
    'api-endpoint': APIEndpoint,
  },
};
</script>



<style scoped >
.root {
  display: flex;
  justify-content: center;
}
.main-content {
  max-width: 1000px;
  width: 100%;
  padding-top: 100px;
  padding-bottom: 100px;
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  /* align-items: center; */
  font-family: "Roboto", sans-serif;
  text-align: start;
}

</style>
