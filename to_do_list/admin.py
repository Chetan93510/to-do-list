from django.contrib import admin
from .models import Gallery
from django.utils.html import format_html

# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['image', 'alt', 'preview']

    def preview(self, obj):
        return format_html(f'<img src="/media/{obj.image}" width="70px">')

admin.site.register(Gallery, GalleryAdmin)