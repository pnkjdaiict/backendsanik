from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
class Blog(models.Model):
    # Title of the blog
    title = models.CharField(max_length=250)
    
    # Short description of the blog
    short_description = models.CharField(max_length=500)
    slug_field = models.SlugField(max_length=500 , unique=True, blank=True, null=True ,)  # Slug field

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
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    meta_title = models.CharField( blank=True, null=True)
    meta_description = models.CharField( blank=True, null=True)
    meta_keywords = models.CharField( blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.slug_field:  # Generate slug only if it's not already set
            self.slug_field = slugify(self.title)
        super().save(*args, **kwargs)  # Call the parent class save method

    def __str__(self):
        return self.title
