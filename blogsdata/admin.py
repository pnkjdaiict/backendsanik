from django.contrib import admin
from .models import Blog
from django.utils.html import format_html
from .form import *
# Create a custom admin class if you need to modify how the model is displayed
class BlogAdmin(admin.ModelAdmin):
    form= BlogForm
    list_display = ('title', 'author', 'status', 'created_at', 'updated_at')  # Columns to display in the list view
    search_fields = ('title', 'author')  # Fields to be searchable
    prepopulated_fields = {'slug_field': ('title',)}  # Automatically populate the slug field from the title
    list_filter = ('status', 'created_at')  # Add filters for status and date
    ordering = ('-created_at',)  # Default ordering by creation date (descending)
    readonly_fields = ('image_preview',)  # Make the image preview read-only
    def image_preview(self, obj):
      
        if obj.image:
            return format_html('<img src="{}" style="width: 550px; height: auto;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Image Preview"  # Column name in the admin interface

# Register the Blog model with the custom admin configuration
admin.site.register(Blog, BlogAdmin)
