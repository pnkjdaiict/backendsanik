from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField

class News(models.Model):
    # Title of the News
    title = models.CharField(max_length=250)
    
    # Short description of the News
    short_description = models.CharField(max_length=500)
    
    # Full content of the News, using a rich text editor
    description = RichTextField()
    
    # Author of the News
    author = models.CharField(max_length=100)
    
    # Date and time when the News was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Date and time when the News was last updated
    updated_at = models.DateTimeField(auto_now=True)
    
    # Status of the News (e.g., Draft, Published)
    status = models.CharField(max_length=20, choices=[
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ], default='draft')

    # Image associated with the News post (optional)
    image = models.ImageField(upload_to='News_images/', null=True, blank=True)

    # Tags related to the News (many-to-many relationship with Tag model)
 

    # SEO Meta fields
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=500, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
