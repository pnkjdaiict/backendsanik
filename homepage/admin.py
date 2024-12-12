from django.contrib import admin
from .models import *
from django.utils.html import format_html
from .forms import *
class BannerAdmin(admin.ModelAdmin):
    fields = (
        'title', 'contact_number', 'facebook_link', 'instagram_link', 'Image',
        'image_preview', 'description', 'meta_title', 'meta_description', 'image_alt', 'meta_keyword'
    )
    list_display = ('title', 'image_preview', 'contact_number')  # Add other fields as needed
   
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.Image:
            return format_html('<img src="{}" id="image-preview"/>', obj.Image.url)
        return format_html('<img id="image-preview" style="display:none;" />')
    image_preview.short_description = 'Image Preview'

admin.site.register(Banner, BannerAdmin)


class TopScrollerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview','image_alt', 'description')  # Fields to display in the list view
    search_fields = ('title', 'description')          
    readonly_fields = ('image_preview',)
    def image_preview(self, obj):
        if obj.Image:
            return format_html('<img src="{}" id="image-preview"/>', obj.Image.url)
    image_preview.short_description = 'Image Preview'
admin.site.register(TopScroller ,TopScrollerAdmin) 

class HomepageImagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview','image_alt', 'description')  # Fields to display in the list view
    search_fields = ('title', 'description')              # Enable search by these fields
    readonly_fields = ('image_preview',)
    def image_preview(self, obj):
        if obj.Image:
            return format_html('<img src="{}" id="image-preview"  style="width: 100px; height: auto;" />', obj.Image.url)
    image_preview.short_description = 'Image Preview'

class EnquiryFormAdmin(admin.ModelAdmin):
    form = EnqForm
    list_display = ('name', 'email' , 'phone' ,'message', )
    search_fields =('name' , 'email' , 'phone' ,  )


admin.site.register(HomePageImages ,HomepageImagesAdmin) 
admin.site.register(LineScrollBar) 
admin.site.register(EnquiryForm,EnquiryFormAdmin)


class SEOAdmin(admin.ModelAdmin):
    list_display = (
        'title',
         'homepagetitle',
        'description',
        'keywords',
        'logo',
        'canonical_url',
        'og_title',
        'og_description',
        'og_image',
        'image_preview',
        'logo_preview',  # Display image preview in the list view
        'og_url',
        'twitter_card',
        'contact_number', 
        'address' ,
        'email'
    )  # Fields to display in the list view
    
    search_fields = ('title', 'description')  # Enable search by these fields
    readonly_fields = ('image_preview','logo_preview'  )  # Make the image preview field read-only

    def image_preview(self, obj):
        if obj.og_image:
            # Ensure you are passing the correct image field `og_image`
            return format_html('<img src="{}" id="image-preview" style="width: 100px; height: auto;" />', obj.og_image.url)
        return "No Image"  # Return a fallback text if no image is provided

    image_preview.short_description = 'Image Preview'  # Customize the column name
    
    def logo_preview(self, obj):
        if obj.logo:
            # Preview for logo
            return format_html(
                '<img src="{}" id="logo-preview" style="width: 100px; height: auto;" />',
                obj.logo.url
            )
        return "No Logo"

# Register the SEO model and the custom admin
admin.site.register(SEO, SEOAdmin)


