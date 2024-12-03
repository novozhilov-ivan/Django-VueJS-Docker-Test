<template>
  <div id="app">
    <h1>Управление изображениями</h1>
    <ImageForm @imageUploaded="fetchImages" />
    <ImageList :images="images" @imageDeleted="fetchImages" />
  </div>
</template>

<script>
import ImageForm from "./components/ImageForm.vue";
import ImageList from "./components/ImageList.vue";
import axios from "axios";

export default {
  components: { ImageForm, ImageList },
  data() {
    return {
      images: [],
    };
  },
  methods: {
    async fetchImages() {
      try {
        const response = await axios.get("http://localhost:8000/api/v1/images");
        this.images = response.data;
      } catch (error) {
        console.error("Error fetching images:", error);
      }
    },
  },
  mounted() {
    this.fetchImages();
  },
};
</script>