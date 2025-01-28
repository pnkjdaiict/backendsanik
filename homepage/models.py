from django.db import models
from courses.models import *
# Create your models here.
from django.db import models 
from ckeditor.fields import RichTextField
class SEO(models.Model):
   
    title = models.CharField(max_length=255, help_text="The title of the page for SEO.")
    homepagetitle = models.CharField(max_length=255, help_text="The home Page Title of the page."  , blank=True, null=True)
    logo = models.ImageField(upload_to='covers/', blank=True, null=True)
    description = models.TextField(help_text="The meta description of the page.")
    keywords = models.CharField(max_length=255, help_text="Comma-separated keywords for SEO.")
    canonical_url = models.URLField(help_text="Canonical URL to avoid duplicate content issues.")
    og_title = models.CharField(max_length=255, help_text="Open Graph title.")
    og_description = models.TextField(help_text="Open Graph description.")
    og_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    og_url = models.URLField(help_text="URL of the page for Open Graph.")
    address =  models.CharField(max_length=255, help_text="The home Page Title of the page."  , blank=True, null=True)
    contact_number = models.CharField(max_length=255 , blank=True , null= True)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True) 
    location = models.CharField(max_length=500 , blank=True , null= True)
    email = models.CharField(max_length=255 , blank=True , null= True)
    scripts = models.TextField(
        blank=True, null=True, help_text="Custom scripts (e.g., tracking, analytics) to embed in the page."
    )  # New field for custom scripts
    twitter_card = models.CharField(
        max_length=255, default="summary_large_image", help_text="Twitter card type."
    )
    

    # Created and Updated Timestamps for better management
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_keywords(self): 
        return self.keywords.split(',') if self.keywords else []

class FAQ(models.Model):
    question = models.CharField()
    answer = models.TextField()
     
    def __str__(self):
        return self.question

class HomepageContent(models.Model):
    details = RichTextField()
    def __str__(self):
        return self.details
      
class Banner(models.Model):
      Image = models.ImageField(upload_to='covers/', blank=True, null=True)
      description = models.CharField(max_length=250 , null=True , blank=True)
      meta_title = models.CharField(max_length =250, null=True ,  blank=True)
      meta_description = models.CharField(max_length=250 , null=True , blank=True)
      image_alt = models.CharField(max_length=250 ,  null=True , blank=True)
      meta_keyword = models.TextField(null=True, blank=True )
      contact_number = models.CharField(max_length=100 , null=True,  blank=True)
      facebook_link = models.CharField(max_length=250 , null=True , blank=True)
      instagram_link = models.CharField(max_length=250 , null=True  ,blank=True)
      title= models.CharField(max_length=250 , null=True) 
      def __str__(self):
        return self.title
      
      def get_meta_keywords(self):
        # Assuming 'meta_keyword' is a string stored in the database
        return self.meta_keyword.split(',') if self.meta_keyword else []
class TopScroller(models.Model):
   Image = models.ImageField(upload_to='covers/', blank=True , null=True)
   image_alt = models.CharField(max_length=255 )
   description = models.CharField(  null=True , blank=True)
   title = models.CharField( null=True ) 
   def __str__(self):
      return self.title
   
class HomePageImages(models.Model):
   Image = models.ImageField(upload_to='covers/' , blank=True)
   image_alt = models.CharField(max_length=250 ,  null=True , blank=True)
   description =   models.CharField(max_length=250 ,  null=True , blank=True)
   meta_keyword = models.TextField(null=True, blank=True )
   contact_number = models.CharField(max_length=100 , null=True,  blank=True)
   facebook_link = models.CharField(max_length=250 , null=True , blank=True)
   instagram_link = models.CharField(max_length=250 , null=True  ,blank=True)
   youtube_link = models.CharField(max_length=250 , null=True  ,blank=True)
   title= models.CharField(max_length=250 , null=True) 
   def __str__(self):
      return self.title
class LineScrollBar(models.Model):
   title = models.CharField(max_length=500)
   link = models.CharField(max_length=500)
   def __str__(self):
      return self.title
   
class EnquiryForm(models.Model):
   type =  models.ManyToManyField(Course, related_name='courses', blank=True)
   name = models.CharField(max_length=200)
   email = models.CharField(max_length=200)
   phone = models.CharField(max_length=50)
   message = models.CharField(max_length=250)
   states = models.CharField(max_length=200, blank=True)
   cities = models.CharField(max_length=200, blank=True)



