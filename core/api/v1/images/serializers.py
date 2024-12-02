from rest_framework import serializers

from core.apps.images.models import ORMImages


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ORMImages
        fields = ["encoded_image", "description"]
