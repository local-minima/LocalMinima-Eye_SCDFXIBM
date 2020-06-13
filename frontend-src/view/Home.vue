<template>
  <div class="root">
    <div class="main-content markdown-body">
      <div v-html="readme"></div>
    </div>
  </div>
</template>

<script>
// import '../styles/dark.min.css';
import MarkdownIt from "markdown-it";
import readmeFile from "../../README.md";

export default {
  name: "Home",
  computed: {},
  data() {
    return {
      readme: ""
    };
  },
  mounted() {
    this.readme = readmeFile;
  }
};
</script>


<style>
li {
  list-style-type: decimal !important;
}

</style>

<style scoped >
.root {
  display: flex;
  justify-content: center;
}
/* .main-content {
  max-width: 1000px;
  padding-top: 100px;
  padding-bottom: 100px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-family: "Roboto", sans-serif;
} */

.markdown-body {
  box-sizing: border-box;
  min-width: 200px;
  max-width: 980px;
  margin: 0 auto;
  padding: 45px;
  list-style-type: decimal !important;
}

@media (max-width: 767px) {
  .markdown-body {
    padding: 15px;
  }
}
</style>
