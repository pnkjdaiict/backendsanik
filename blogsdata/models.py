from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Blog(models.Model):
    # Title of the blog
    title = models.CharField(max_length=250)
    
    # Slug field that will be auto-generated from the title
    slug_field = models.SlugField(null=True, blank=True, unique=True)  # Unique constraint added for slug
    
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
    
    # Status of the blog (e.g., Draft, Published, Archived)
    status = models.CharField(
        max_length=20,
        choices=[
            ('draft', 'Draft'),
            ('published', 'Published'),
            ('archived', 'Archived'),
        ],
        default='draft'
    )
    
    # Image associated with the blog post (optional)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    
    # SEO Meta fields
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.CharField(max_length=500, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Automatically set the slug field if it is empty
        if not self.slug_field:
            self.slug_field = slugify(self.title)  # Slug generated from the title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
