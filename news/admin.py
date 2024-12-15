from django.contrib import admin
from .models import *
# Register your models here.
from django.utils.html import format_html
from .forms import *
class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    list_display = ('title', 'author', 'status', 'created_at', 'updated_at', 'image_preview')  # Customize the fields displayed
    list_filter = ('status', 'created_at', 'updated_at')  # Add filters for easier navigation
    search_fields = ('title', 'author', 'short_description')  # Add search functionality
    readonly_fields = ('image_preview',)  # Make the image preview read-only

    def image_preview(self, obj):
      
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Image Preview"  # Column name in the admin interface

# Register News and Tag in admin
# admin.site.register(News, NewsAdmin)
