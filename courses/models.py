from django.db import models
from states.models import *
# Create your models here.
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Course(models.Model):
    title = models.CharField(max_length=255 , help_text="enter title")
    short_title = models.CharField(max_length=255  , blank=True, null=True ,)
    short_description = models.CharField(max_length=250)
    slug_field = models.SlugField(unique=True, blank=True, null=True ,)  # Slug field
    description = RichTextField()
    image = models.ImageField(upload_to='covers/', blank=True, null=True)
    image_alt = models.CharField(max_length=250, null=True, blank=True)
    states = models.ManyToManyField(State, related_name='courses')
    cities = models.ManyToManyField(Cities, related_name='courses' )
    localities = models.ManyToManyField(Localities , related_name='localities')
    course_code = models.CharField(max_length=100, unique=True, null=True, blank=True)
    meta_keyword = models.TextField(null=True, blank=True )
    contact_number = models.CharField(max_length=100 , null=True,  blank=True)
    youtube_link=models.CharField(max_length=250 , null=True , blank=True)
    facebook_link = models.CharField(max_length=250 , null=True , blank=True)
    instagram_link = models.CharField(max_length=250 , null=True  ,blank=True)
    meta_title = models.CharField(max_length =500, null=True ,  blank=True)
    meta_description = models.CharField(max_length=500 , null=True , blank=True)
    def save(self, *args, **kwargs):
        if not self.slug_field:  # Generate slug only if it's not already set
            self.slug_field = slugify(self.title)
        super().save(*args, **kwargs)  # Call the parent class save method

    def __str__(self):
        return self.title
    
class CourseSeoData(models.Model):
    meta_title = models.CharField(max_length=250, null=True, blank=True)
    meta_description = models.CharField(max_length=250, null=True, blank=True)
    meta_keywords = models.TextField(null=True, blank=True)
    og_title = models.CharField(max_length=250, null=True, blank=True)
    og_description = models.CharField(max_length=250, null=True, blank=True)
    og_image = models.ImageField(upload_to="og_images/", null=True, blank=True)
    twitter_card = models.CharField(
        max_length=50, 
        choices=[("summary", "Summary"), ("summary_large_image", "Summary Large Image")],
        default="summary",
        null=True, 
        blank=True
    )
    
    def __str__(self):
        return self.meta_title or "SEO Data"
class SubCourse(models.Model):
    title = models.CharField(max_length=255)
    slug_field =models.SlugField(unique=True, blank=True, null=True ,  )
    short_description = models.CharField(max_length=250)
    description = RichTextField()
    image = models.ImageField(upload_to='covers/', blank=True, null=True )
    image_alt = models.CharField(max_length=250, null=True, blank=True)
    course_code = models.CharField(max_length=100, unique=True, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    meta_keyword = models.TextField(null=True, blank=True )
    contact_number = models.CharField(max_length=100 , null=True,  blank=True)
    facebook_link = models.CharField(max_length=250 , null=True , blank=True)
    instagram_link = models.CharField(max_length=250 , null=True  ,blank=True)
    youtube_link = models.CharField(max_length=250 , null=True  ,blank=True)
    meta_title = models.CharField(max_length =250, null=True ,  blank=True)
    meta_description = models.CharField(max_length=250 , null=True , blank=True)
    courses  = models.ManyToManyField(Course, related_name='coursesn', blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug_field:  # Generate slug only if it's not already set
            self.slug_field = slugify(self.title)
        super().save(*args, **kwargs)  # Call the parent class save method

    def __str__(self):
        return self.title
class Image(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='course_images/')
    image_alt = models.CharField(max_length=250, null=True, blank=True)
    meta_keyword = models.TextField(null=True, blank=True )
    contact_number = models.CharField(max_length=100 , null=True,  blank=True)
    youtube_link=models.CharField(max_length=250 , null=True , blank=True)
    facebook_link = models.CharField(max_length=250 , null=True , blank=True)
    instagram_link = models.CharField(max_length=250 , null=True  ,blank=True)
    meta_title = models.CharField(max_length =250, null=True ,  blank=True)
    meta_description = models.CharField(max_length=250 , null=True , blank=True)  
    def __str__(self):
        return f"Image for {self.course.title}"
class SubCourseImage(models.Model):
    course = models.ForeignKey(SubCourse, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='Subcourse_images/')
    image_alt = models.CharField(max_length=250, null=True, blank=True)
    meta_keyword = models.TextField(null=True, blank=True )
    contact_number = models.CharField(max_length=100 , null=True,  blank=True)
    youtube_link=models.CharField(max_length=250 , null=True , blank=True)
    facebook_link = models.CharField(max_length=250 , null=True , blank=True)
    instagram_link = models.CharField(max_length=250 , null=True  ,blank=True)
    meta_title = models.CharField(max_length =250, null=True ,  blank=True)
    meta_description = models.CharField(max_length=250 , null=True , blank=True)
     
    def __str__(self):
        return f"Image for {self.course.title}"
class SubCategory(models.Model):

    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=250, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='covers/', blank=True, null=True)
    image_alt = models.CharField(max_length=250, null=True, blank=True)
    subcourse = models.ManyToManyField(SubCourse , null=True, blank=True ,  related_name='subcategories')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    meta_keyword = models.TextField(null=True, blank=True)
    contact_number = models.CharField(max_length=100, null=True, blank=True)
    youtube_link = models.CharField(max_length=250, null=True, blank=True)
    facebook_link = models.CharField(max_length=250, null=True, blank=True)
    instagram_link = models.CharField(max_length=250, null=True, blank=True)
    meta_title = models.CharField(max_length=250, null=True, blank=True)
    meta_description = models.CharField(max_length=250, null=True, blank=True)
    
    def __str__(self): 
        return self.title  
class multiple_title(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='multiple_title')
    title = models.TextField(null=True, blank=True )
    def __str__(self):
          
          return self.title
class multiple_descriptions(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='multiple_description')
    title =  models.TextField(null=True, blank=True , default="new" )
    description = RichTextField() 

class multiple_images(models.Model):
    title = models.CharField(max_length=500 , null= True , blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='multiple_imagess')
    imagess = models.ImageField(upload_to='covers/', blank=True, null=True)
    image_alt = models.CharField(max_length=500, null=True, blank=True)
    contact_number = models.CharField(max_length=100 , null=True,  blank=True)
    meta_title = models.CharField(max_length =500, null=True ,  blank=True)
    meta_description = models.CharField(max_length=500 , null=True , blank=True)  
    meta_keyword = models.TextField(null=True, blank=True )
     