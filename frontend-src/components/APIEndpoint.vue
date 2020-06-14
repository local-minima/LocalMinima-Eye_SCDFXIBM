<template>
  <div class="main markdown-body">
    <h1>
      API endpoint |
      <code>{{url}}</code>
    </h1>
    <div>
      <div>

        <h2 v-if="sample2">
          Upload Your Image (or use
          <a @click="useDemo(sample1)">Demo1</a> or 
          <a @click="useDemo(sample2)">Demo2</a>)
        </h2>
        <h2 v-if="!sample2">
          Upload Your Image (or use
          <a @click="useDemo(sample1)">Demo</a>)
        </h2>
        <input type="file" id="img" ref="file" @change="onUpload" />
      </div>
      <br />
      <div id="preview-box">
        <img id="preview" :src="previewSrc" />
      </div>
      <div>
        <h2>Result</h2>
        <code v-html="results"></code>
      </div>
    </div>
    <br />
    <hr />
    <!-- <button @click="sendRequest">Send</button> -->
    <canvas id="c" ref="canvas"></canvas>
    <img id="i" :src="previewSrc" ref="i" @load="onNewImage" />
  </div>
</template>

<script>
import axios from "axios";

function syntaxHighlight(json) {
  if (typeof json != 'string') {
    json = JSON.stringify(json, undefined, 2);
  }
  json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
    var cls = 'number';
    if (/^"/.test(match)) {
      if (/:$/.test(match)) {
        cls = 'key';
      } else {
        cls = 'string';
      }
    } else if (/true|false/.test(match)) {
      cls = 'boolean';
    } else if (/null/.test(match)) {
      cls = 'null';
    }
    return '<span class="' + cls + '">' + match + '</span>';
  });
}

export default {
  name: "api-endpoint",
  props: ['url', 'sample1','sample2'],
  data() {
    return {
      previewSrc: "",
      imagePicked: false,
      results: '',
    };
  },
  watch: {
    previewSrc() {
      this.results = 'loading...';
    }
  },
  methods: {
    
    async sendRequest() {
      // var imagefile = document.querySelector("#file");
      // formData.append("image", imagefile.files[0]);
      // axios.post("upload_file", formData, {
      //   headers: {
      //     "Content-Type": "multipart/form-data"
      //   }
      // });
      // await axios.post("https://scdfxibm2020.garykim.dev/traffic", {});
      console.log('hi');
      
      let data = new FormData();
      this.$refs.canvas.toBlob(function(blob) {
        console.log(blob);
        
        data.append("file", blob);

        axios
          .post(this.url, data, {
            headers: {
              "Content-Type": "multipart/form-data"
            }
          })
          .then(function(res) {
            console.log(syntaxHighlight(res.data));
            
            this.results = syntaxHighlight(res.data);
          }.bind(this));
      }.bind(this));
    },
    useDemo(url) {
      this.previewSrc = url;
      this.imagePicked = true;
    },
    onUpload() {
      if (this.$refs.file.files && this.$refs.file.files[0]) {
        console.log(this.$refs.file.files[0]);

        this.previewSrc = URL.createObjectURL(this.$refs.file.files[0]);
        this.imagePicked = true;
      }
    },
    onNewImage() {
      const c = this.$refs.canvas;
      const i = this.$refs.i;
      const width = (c.width = i.width);
      const height = (c.height = i.height);
      const ctx = c.getContext("2d");
      console.log(ctx);
      ctx.drawImage(i, 0, 0);
      console.log('hi');
      
      this.sendRequest();

    }
  }
};
</script>

<style scoped>
#c,
#i {
  display: none;
}
.main a {
  cursor: pointer;
  color: #0366d6 !important;
}
.main a:visited {
  color: #0366d6 !important;
}
#preview {
  max-width: 600px;
  max-height: 600px;
  object-fit: cover;
}

</style>
