from django.contrib import admin

from core.apps.images.models import ORMImages


@admin.register(ORMImages)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "base64_payload",
        "extension",
        "description",
        "created_at",
        "updated_at",
    )
