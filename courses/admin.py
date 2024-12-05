from django.contrib import admin
from .models import *
from django.utils.html import format_html
from .forms import *
class ImageInline(admin.StackedInline):
    model = Image
    fields = ('image', 'image_alt', 'meta_keyword' , 'contact_number' , 'youtube_link' , 'facebook_link', 'instagram_link' , 'meta_title' , 'meta_description')  # Replace with your model's fields
    
    classes = ('collapse',)  # Optional: Makes it collapsible in admin panel

    extra = 1  # Number of empty image fields to display
class SubCourseImages(admin.StackedInline):
    model = SubCourseImage
    fields = ('image', 'image_alt', 'meta_keyword' , 'contact_number' , 'youtube_link' , 'facebook_link', 'instagram_link' , 'meta_title' , 'meta_description')  # Replace with your model's fields
    
    classes = ('collapse',)  # Optional: Makes it collapsible in admin panel

    extra = 1  # Number of empty image fields to display
 
class CoursesAdmin(admin.ModelAdmin):
    class Media:
      js = ('js/slugify.js',) 
    form = CourseForm
    inlines = [ImageInline ]
    prepopulated_fields = {'slug_field': ('title',)}
    
    fields = (
          'title','short_description','slug_field' ,'description', 'image', 'image_alt', 'course_code'  , 'states' ,'cities', 'localities' ,'meta_keyword' ,  'meta_title' , 'meta_description',
            'contact_number',
            'facebook_link',
            'instagram_link',
            'youtube_link',)
    list_display = ('title', 'slug_field','image_preview', 'short_description','course_code',  'contact_number' ,)  # Add other fields as needed
    search_fields = ('title', 'course_code',)    
    readonly_fields = ('image_preview',)  # Make the slug field readonly (optional)
    
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" id="image-preview" style="display:block; width:100px    "/>', obj.image.url)
        return format_html('<img id="image-preview" style="display:none; width:100px    " />')
    image_preview.short_description = 'Image Preview'

class SubCoursesAdmin(admin.ModelAdmin):
    form = SubCourseForm
    inlines = [SubCourseImages ]
    fields = (
        'title', 'short_description', 'description', 'image',  'image_alt','image_preview', 'course_code', 'price', 'courses', 'meta_keyword',  'meta_title' , 'meta_description', 'contact_number', 'facebook_link' , 'instagram_link', 'youtube_link'  ,
    )
    list_display = ('title','image_preview', 'short_description' ,'course_code' ,'contact_number' )
    search_fields = ('title', 'course_code')    
    readonly_fields = ('image_preview','slug_field')  # Make the slug field readonly (optional)
    
    def image_preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return format_html('<img src="{}" id="image-preview"  style="width: 100px; height: auto;"/>', obj.image.url)
        # return format_html('<img id="image-preview" style="display:none; width: 100px; height: auto; />')
        
        return  format_html('<img src="{}" id="image-preview"  style="width: 100px; height: auto;" />', obj.image.url)
    image_preview.short_description = 'Image Preview'

class SubCategoryAdmin(admin.ModelAdmin):
    form = SubCategoriesForm
    
 
#  SubCategoriesForm

admin.site.register(Course ,CoursesAdmin)
admin.site.register(SubCourse ,SubCoursesAdmin)
admin.site.register(SubCategory ,SubCategoryAdmin)

