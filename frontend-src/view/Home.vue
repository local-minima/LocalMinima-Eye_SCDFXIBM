<template>
  <div class="root">
    <cv-header aria-label="Carbon header">
      <cv-header-menu-button aria-label="Header menu" aria-controls="side-nav" />
      <cv-skip-to-content href="#main-content">Skip to content</cv-skip-to-content>
      <cv-header-name href="javascript:void(0)" prefix="IBM">[Platform]</cv-header-name>
      <cv-header-nav aria-label="Carbon nav">
        <cv-header-menu-item href="javascript:void(0)">Link 1</cv-header-menu-item>
        <cv-header-menu-item href="javascript:void(0)">Link 2</cv-header-menu-item>
        <cv-header-menu-item href="javascript:void(0)">Link 3</cv-header-menu-item>
        <cv-header-menu aria-label="Link 4" title="Link 4">
          <cv-header-menu-item href="javascript:void(0)">Submenu Link 1</cv-header-menu-item>
          <cv-header-menu-item href="javascript:void(0)">Submenu Link 2</cv-header-menu-item>
          <cv-header-menu-item href="javascript:void(0)">Submenu Link 3</cv-header-menu-item>
        </cv-header-menu>
      </cv-header-nav>
      <template slot="left-panels">
        <cv-side-nav id="side-nav" fixed>
          <cv-side-nav-items>
            <cv-header-side-nav-items>
              <cv-header-menu-item href="javascript:void(0)">Link 1</cv-header-menu-item>
              <cv-header-menu-item href="javascript:void(0)">Link 2</cv-header-menu-item>
              <cv-header-menu-item href="javascript:void(0)">Link 3</cv-header-menu-item>
              <cv-header-menu aria-label="Link 4" title="Link 4" :hover-toggle="false">
                <cv-header-menu-item href="javascript:void(0)">Submenu Link 1</cv-header-menu-item>
                <cv-header-menu-item href="javascript:void(0)">Submenu Link 2</cv-header-menu-item>
                <cv-header-menu-item href="javascript:void(0)">Submenu Link 3</cv-header-menu-item>
              </cv-header-menu>
            </cv-header-side-nav-items>
          </cv-side-nav-items>
        </cv-side-nav>
      </template>
      <template slot="right-panels"></template>
    </cv-header>
    <div class="main-content">
      <h1>hello world</h1>
      <br>
      <CvButton>Button</CvButton>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  computed: {}
};
</script>

<style lang="less" scoped>
.main-content {
  padding-top: 100px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
