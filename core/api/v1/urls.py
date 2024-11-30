from django.urls import path

from .images.handlers.add_image import AddImageAPIView
from .images.handlers.get_images import GetImageListAPIView
from .images.handlers.remove_image import DeleteImageAPIView


urlpatterns = [
    path(
        "image/",
        AddImageAPIView.as_view(),
        name="Добавить новое изображение",
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
