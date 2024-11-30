from django.contrib import admin

from core.apps.images.models import Images


@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "encoded_image", "description", "created_at", "updated_at")
