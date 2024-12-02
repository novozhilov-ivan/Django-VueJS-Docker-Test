from rest_framework import generics

from core.api.v1.images.serializers import ImagesSerializer


class AddImageAPIView(generics.ListCreateAPIView):
    serializer_class = ImagesSerializer

    # TODO получение списка изображений, добавление, удаление по id
