from django.urls import path

from .images.add_image.handler import add_image_handler
from .images.handlers.get_images import GetImageListAPIView
from .images.handlers.remove_image import DeleteImageAPIView


urlpatterns = [
    path(
        "image/",
        add_image_handler,
        name="add_image",
    ),
    path(
        "image/",
        DeleteImageAPIView.as_view(),
        name="Удалить изображение по id",
    ),
    path(
        "images/",
        GetImageListAPIView.as_view(),
        name="Получить список изображений",
    ),
]
