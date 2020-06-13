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

<style>
a.bx--header__menu-item[aria-current='page']::after, .bx--header__menu-item--current::after {

  border-bottom: 3px solid #95dfcc !important;
}
</style>

<style lang="less" scoped>
#router {
  padding-top: 48px;
}
</style>
