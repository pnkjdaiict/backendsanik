from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    # Title of the blog
    title = models.CharField(max_length=250)
    
    # Short description of the blog
    short_description = models.CharField(max_length=500)
    
    # Full content of the blog, using a rich text editor
    description = RichTextField()
    
    # Author of the blog
    author = models.CharField(max_length=100)
    
    # Date and time when the blog was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Date and time when the blog was last updated
    updated_at = models.DateTimeField(auto_now=True)
    
    # Status of the blog (e.g., Draft, Published)
    status = models.CharField(max_length=20, choices=[
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ], default='draft')

    # Image associated with the blog post (optional)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    # Tags related to the blog (many-to-many relationship with Tag model)
 

    # SEO Meta fields
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=500, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
