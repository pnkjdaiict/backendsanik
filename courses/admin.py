from django.contrib import admin
from .models import *
from django.utils.html import format_html
from .forms import *
class multiImagesline(admin.StackedInline):
    model = multiple_Images
    form = ImageForm
    fields = ( "title" , 
    "course"  ,
    "image"  ,
    "image_alt" ,
    "contact_number" ,
    "meta_title"  ,
    "meta_description"  ,
    "image_preview" ,
    "meta_keyword")   # Replace with your model's fields
    classes = ('collapse',)  # Optional: Makes it collapsible in admin panel
    extra = 1  # Number of empty image fields to display
    readonly_fields = ('image_preview',)

    # Adding a preview of the image in the admin list view
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" id="image-preview" style="display:block; width:100px;"/>', obj.image.url)
        return format_html('<img id="image-preview" style="display:none; width:100px;"/>')
    image_preview.short_description = 'Image Preview' 
  
class DescriptionInline(admin.StackedInline):
    model = multiple_descriptions
    
    fields = ('id', 'title','description')  
    classes = ('collapse',)   
    extra = 1  
class TitleInline(admin.StackedInline):
    model = multiple_title
    form = multititleForm
    fields = (   'id', 'title',)  
    classes = ('collapse',)   
    extra = 1  
class ImageInline(admin.StackedInline):
    model = Image
    form = ImageForm
    fields = ('image', 'image_alt', 'meta_keyword' , 'contact_number' , 'youtube_link' , 'facebook_link', 'instagram_link' , 'meta_title' , 'meta_description')  # Replace with your model's fields
    classes = ('collapse',)  # Optional: Makes it collapsible in admin panel
    
    extra = 1  # Number of empty image fields to display
    
class SubCourseImages(admin.StackedInline):
    model = SubCourseImage
    fields = ('image', 'image_alt', 'meta_keyword' , 'contact_number' , 'youtube_link' , 'facebook_link', 'instagram_link' , 'meta_title' , 'meta_description')  # Replace with your model's fields
    
    classes = ('collapse',)  # Optional: Makes it collapsible in admin panel

    extra = 1  # Number of empty image fields to display
 
 
class CoursesAdmin(admin.ModelAdmin):
    # Loading the JavaScript for the "Select All" functionality
    
    # Customizing the form for the Course model
    form = CourseForm

    # Inlines used for the Course model
    inlines = [ImageInline, TitleInline, DescriptionInline, multiImagesline]
  # You may want to review this if TabularInline is meant for something specific

    # Automatically populate the slug field from the title
    prepopulated_fields = {'slug_field': ('title',)}

    # Defining the fields to display in the admin form
    fields = (
        'title', 'short_title', 'short_description', 'slug_field', 'description', 'image', 'image_alt', 
        'course_code', 'states', 'cities', 'localities', 'meta_keyword', 'meta_title', 
        'meta_description', 'contact_number', 'facebook_link', 'instagram_link', 'youtube_link',
    )

    # Defining the columns to display in the list view
    list_display = (
        'title', 'slug_field', 'image_preview', 'short_description', 'course_code', 'contact_number',
    )

    # Fields to search in the admin search bar
    search_fields = ('title', 'course_code',)

    # Fields that are read-only (in this case, the image preview)
    readonly_fields = ('image_preview',)

    # Adding a preview of the image in the admin list view
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" id="image-preview" style="display:block; width:100px;"/>', obj.image.url)
        return format_html('<img id="image-preview" style="display:none; width:100px;"/>')
    image_preview.short_description = 'Image Preview'

# Registering the model admin
admin.site.register(Course, CoursesAdmin)

# class CoursesAdmin(admin.ModelAdmin):
#     class Media:
#       js = ('js/slugify.js',) 
      
#     form = CourseForm
#     inlines = [ImageInline ,TitleInline,DescriptionInline  ,multiImagesline]
#     TabularInline= [multiImagesline ,multiImagesline]
#     prepopulated_fields = {'slug_field': ('title',)}
#     fields = (
#           'title', 'short_title','short_description','slug_field' ,'description', 'image', 'image_alt', 'course_code'  , 'states' ,'cities', 'localities' ,'meta_keyword' ,  'meta_title' , 'meta_description', 'contact_number',  'facebook_link', 'instagram_link',         'youtube_link',)
#     list_display = ('title', 'slug_field','image_preview', 'short_description','course_code',  'contact_number' ,) 
#     search_fields = ('title', 'course_code',)    
#     readonly_fields = ('image_preview',)
    
    
#     def image_preview(self, obj):
#         if obj.image:
#             return format_html('<img src="{}" id="image-preview" style="display:block; width:100px    "/>', obj.image.url)
#         return format_html('<img id="image-preview" style="display:none; width:100px    " />')
#     image_preview.short_description = 'Image Preview'

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
    
class CourseSeoDataAdmin(admin.ModelAdmin):
    list_display = ('meta_title', 'meta_description', 'twitter_card', 'og_image_preview')
    list_filter = ('twitter_card',)
    search_fields = ('meta_title', 'meta_description', 'meta_keywords', 'og_title', 'og_description')
    readonly_fields = ('og_image_preview',)  # Make the preview field read-only
    form =CourseSeoDataForm
    def og_image_preview(self, obj):
        """
        Returns an HTML snippet for displaying the image preview in the admin.
        """
        if obj.og_image:
            return format_html(
                '<img src="{}" style="max-width: 150px; max-height: 150px;" alt="OG Image Preview"/>',
                obj.og_image.url,
            )
        return "No Image"

    og_image_preview.short_description = "OG Image Preview"

admin.site.register(CourseSeoData, CourseSeoDataAdmin)
# admin.site.register(Course ,CoursesAdmin)
admin.site.register(SubCourse ,SubCoursesAdmin)
admin.site.register(SubCategory ,SubCategoryAdmin)

