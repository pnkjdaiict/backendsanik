from django.db import models
from states.models import *
# Create your models here.



# SubCourses Model
class SubCourse(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='covers/', blank=True, null=True)
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
   
    def __str__(self):
        return self.title
class Course(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='covers/', blank=True, null=True)
    image_alt = models.CharField(max_length=250, null=True, blank=True)
    states = models.ManyToManyField(State, related_name='courses')
    cities = models.ManyToManyField(Cities, related_name='courses')
    course_code = models.CharField(max_length=100, unique=True, null=True, blank=True)
    SubCourses = models.ManyToManyField(SubCourse, related_name='courses', blank=True)
    meta_keyword = models.TextField(null=True, blank=True )
    contact_number = models.CharField(max_length=100 , null=True,  blank=True)
    youtube_link=models.CharField(max_length=250 , null=True , blank=True)
    facebook_link = models.CharField(max_length=250 , null=True , blank=True)
    instagram_link = models.CharField(max_length=250 , null=True  ,blank=True)
    meta_title = models.CharField(max_length =250, null=True ,  blank=True)
    meta_description = models.CharField(max_length=250 , null=True , blank=True)
    
    def __str__(self):
        return self.title