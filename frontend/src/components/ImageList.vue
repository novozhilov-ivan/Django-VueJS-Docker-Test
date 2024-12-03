<template>
  <div>
    <h2>Список изображений</h2>
    <ul v-if="images.length > 0">
      <li v-for="image in images" :key="image.id">
        <p><strong>Описание:</strong> {{ image.description }}</p>
        <img
          :src="'data:image/' + image.extension + ';base64,' + image.base64_payload"
          :alt="image.description"
          style="max-width: 200px; max-height: 200px; display: block; margin-bottom: 10px;"
        />
        <button @click="deleteImage(image.id)">Удалить</button>
      </li>
    </ul>
    <p v-else>Нет доступных изображений.</p>
  </div>
</template>

<script>
export default {
  props: ["images"], // Массив изображений, переданный от родительского компонента
  methods: {
    /**
     * Удаление изображения по ID
     * @param {number} id
     */
    async deleteImage(id) {
      try {
        // Отправляем DELETE-запрос на сервер
        await this.$axios.delete(`image/${id}`);
        this.$emit("imageDeleted"); // Уведомляем родительский компонент об изменении
      } catch (error) {
        console.error("Ошибка при удалении изображения:", error);
      }
    },
  },
};
</script>
