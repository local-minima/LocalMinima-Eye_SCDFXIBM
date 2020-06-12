<template>
  <div id="app">
    <navbar/>
    <router-view id="router"/>
  </div>
</template>

<script>
import Navbar from '../components/Navbar'

export default {
  name: "App",
  components: {
    'navbar': Navbar,
  }
};
</script>

<style lang="less" scoped>
#router {
  padding-top: 48px;
}
</style>
