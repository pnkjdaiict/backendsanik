# models.py in the 'courselist' app
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Defining the 'mainCourse' model
class mainCourse(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=250)
    description = RichTextField(null=True, blank=True)
    meta_keyword = models.TextField(null=True, blank=True)
    contact_number = models.CharField(max_length=100, null=True, blank=True)
    facebook_link = models.CharField(max_length=250, null=True, blank=True)
    instagram_link = models.CharField(max_length=250, null=True, blank=True)
    youtube_link = models.CharField(max_length=250, null=True, blank=True)
    meta_title = models.CharField(max_length=250, null=True, blank=True)
    meta_description = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slugfield:  # Generate slug only if it's not already set
            self.slugfield = slugify(self.title)
        super().save(*args, **kwargs)  # Call the parent class save method

    def __str__(self):
        return self.title

# Image model which references 'mainCourse'
class Image(models.Model):
    image = models.ImageField(upload_to='course_images/')
    alt_text = models.CharField(max_length=250, null=True, blank=True)
    course = models.ForeignKey(mainCourse, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.alt_text or str(self.image)
