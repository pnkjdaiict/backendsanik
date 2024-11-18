from django.contrib import admin
from .models import *
# Register your models here.
from django.utils.html import format_html
from .forms import CourseForm
  
class CoursesAdmin(admin.ModelAdmin):
    form = CourseForm
    fields = (
          'title', 'short_description', 'description', 'image','image_preview' , 'image_alt', 'course_code', 'SubCourses', 'states' ,'cities' ,'meta_keyword',
            'contact_number',
            'facebook_link',
            'instagram_link',
            'youtube_link', )
    list_display = ('title', 'image_preview', 'short_description','course_code',  'contact_number')  # Add other fields as needed
    search_fields = ('title', 'course_code')    
    readonly_fields = ('image_preview',)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" id="image-preview" style="display:block; width:100px    "/>', obj.image.url)
        return format_html('<img id="image-preview" style="display:none; width:100px    " />')
    image_preview.short_description = 'Image Preview'

class SubCoursesAdmin(admin.ModelAdmin):
    fields = (
        'title', 'short_description', 'description', 'image', 'image_alt', 'course_code', 'price',  'meta_keyword',
            'contact_number',
            'facebook_link',
            'instagram_link',
            'youtube_link'
    )
    list_display = ('title','image_preview', 'short_description' ,'course_code' ,'contact_number' )
    search_fields = ('title', 'course_code')    
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" id="image-preview"  style="width: 100px; height: auto;"/>', obj.image.url)
        # return format_html('<img id="image-preview" style="display:none; width: 100px; height: auto; />')
        
        return  format_html('<img src="{}" id="image-preview"  style="width: 100px; height: auto;" />', obj.Image.url)
    image_preview.short_description = 'Image Preview'
 
admin.site.register(Course ,CoursesAdmin)
admin.site.register(SubCourse ,SubCoursesAdmin)
