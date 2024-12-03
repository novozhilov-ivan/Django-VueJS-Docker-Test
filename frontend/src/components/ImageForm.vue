<template>
  <div>
    <h2>Загрузить изображение</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label>Описание:</label>
        <input v-model="description" required />
      </div>
      <div>
        <label>Изображение:</label>
        <input type="file" @change="handleFile" accept="image/png, image/jpeg, image/gif" required />
      </div>
      <button type="submit">Загрузить</button>
    </form>
  </div>
</template>

<script>

export default {
  data() {
    return {
      description: "", // Описание изображения
      file: null,      // Выбранный файл
      extension: "",   // Расширение файла
    };
  },
  methods: {
    /**
     * Обработка выбора файла
     * @param {Event} event
     */
    handleFile(event) {
      const file = event.target.files[0];
      if (file) {
        this.file = file;

        // Определение расширения файла и преобразование в значения перечисления
        const rawExtension = file.name.split(".").pop().toLowerCase();
        switch (rawExtension) {
          case "jpg":
          case "jpeg":
            this.extension = "jpeg";
            break;
          case "png":
            this.extension = "png";
            break;
          case "gif":
            this.extension = "gif";
            break;
          default:
            alert("Поддерживаются только изображения форматов PNG, JPEG и GIF.");
            this.file = null;
            this.extension = "";
            return;
        }
      }
    },

    /**
     * Отправка данных на сервер
     */
    async submitForm() {
      if (!this.file || !this.extension) {
        alert("Выберите файл подходящего формата!");
        return;
      }

      // Конвертация файла в Base64
      const reader = new FileReader();
      reader.onload = async () => {
        const base64Payload = reader.result.split(",")[1];

        try {
          // Отправка данных на сервер на правильный путь
          await this.$axios.post("image/", {
            base64_payload: base64Payload,
            extension: this.extension, // Используем значение из перечисления
            description: this.description,
          });

          // Уведомление родительского компонента об успешной загрузке
          this.$emit("imageUploaded");

          // Сброс формы
          this.description = "";
          this.file = null;
          this.extension = "";
        } catch (error) {
          console.error("Ошибка при загрузке изображения:", error);
        }
      };
      reader.readAsDataURL(this.file);
    },
  },
};
</script>
