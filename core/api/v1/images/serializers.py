from rest_framework import serializers

from core.apps.images.models import Images


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["encoded_image", "description"]
