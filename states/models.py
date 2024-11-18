from django.db import models

# Create your models here.

class State(models.Model):
    title = models.CharField(max_length=150 ,  null=True , blank=True)
    description = models.TextField(max_length=500 ,  null=True , blank=True)
    short_description = models.TextField(max_length=250 ,  null=True , blank=True)
    Image = models.ImageField(upload_to='covers/', blank=True, null=True)
    image_alt = models.CharField(max_length=250 ,  null=True , blank=True)
    meta_keyword = models.TextField(null=True, blank=True )
    contact_number = models.CharField(max_length=100 , null=True,  blank=True)
    facebook_link = models.CharField(max_length=250 , null=True , blank=True)
    instagram_link = models.CharField(max_length=250 , null=True  ,blank=True)
    meta_title = models.CharField(max_length =250, null=True ,  blank=True)
    meta_description = models.CharField(max_length=250 , null=True , blank=True)

    def __str__(self) :
      return self.title
    
class Cities(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')  # ForeignKey to State
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    short_description = models.TextField(max_length=250, null=True, blank=True)
    Image = models.ImageField(upload_to='covers/', blank=True, null=True)
    image_alt = models.CharField(max_length=250, null=True, blank=True)
    meta_keyword = models.TextField(null=True, blank=True)
    contact_number = models.CharField(max_length=100, null=True, blank=True)
    facebook_link = models.CharField(max_length=250, null=True, blank=True)
    instagram_link = models.CharField(max_length=250, null=True, blank=True)
    meta_title = models.CharField(max_length=250, null=True, blank=True)
    meta_description = models.CharField(max_length=250, null=True, blank=True)
    
    def __str__(self):
        return self.title