from django.db import models

# Create your models here.

class State(models.Model):
    title = models.CharField(max_length=150 ,  null=True , blank=True )
    description = models.TextField(max_length=500 ,  null=True , blank=True ,)
    short_description = models.TextField(max_length=250 ,  null=True , blank=True  , help_text="institute name")
    Image = models.ImageField(upload_to='covers/', blank=True, null=True)
    image_alt = models.CharField(max_length=250 ,  null=True , blank=True)
    meta_keyword = models.TextField(null=True, blank=True )
    contact_number = models.CharField(max_length=100 , null=True,  blank=True , default="8619453001")
    Whatsapp_number = models.CharField(max_length=100 , null=True,  blank=True ,default="8278640248")
    facebook_link = models.CharField(max_length=250 , null=True , blank=True , default="https://www.facebook.com/Sainikschoolentranceexamcoaching/" )
    youtube_link = models.CharField(max_length=250 , null=True , blank=True , default="https://www.youtube.com/@rdajaipur")
    instagram_link = models.CharField(max_length=250 , null=True  ,blank=True,  default="https://www.instagram.com/onlinesainikschoolcoaching/")
    meta_title = models.CharField(max_length =250, null=True ,  blank=True , )
    meta_description = models.CharField(max_length=250 , null=True , blank=True )
    latitude   = models.CharField( null=True, blank=True)
    logitude  = models.CharField( null=True, blank=True)
    pincode = models.CharField( null=True, blank=True)
    
    def __str__(self) :
      return self.title
    
class Cities(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities' )  # ForeignKey to State
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True , default="Top Coaching for Sainik School location , RMS, and RIMC Entrance Exams Join the best coaching center for Sainik School location , Rashtriya Military School (RMS), and RIMC entrance exams location. Achieve your dream of joining prestigious military schools with our expert guidance and proven success strategies location")
    short_description = models.TextField( null=True, blank=True , default="Expert coaching for Sainik School location, Rashtriya Military School (RMS), and RIMC entrance exams location. Comprehensive preparation, experienced faculty, and proven results location")
    Image = models.ImageField(upload_to='covers/', blank=True, null=True)
    image_alt = models.CharField( null=True, blank=True , default="Sainik School, RMS, and RIMC Entrance Exams")
    meta_keyword = models.TextField(null=True, blank=True ,default="sainik school coaching location , rashtriya military school coaching location, rms entrance exam coaching, rimc coaching, military school entrance exam coaching, sainik school entrance exam coaching, rashtriya military school entrance exam, rimc entrance exam coaching, military school coaching location, rms coaching, sainik school coaching, rimc coaching, military entrance exam preparation location")
    contact_number = models.CharField(max_length=100, null=True, blank=True , default="8769422006")
    whatsapp_number = models.CharField(max_length=100 , null=True,  blank=True ,default="8278640248")
    facebook_link = models.CharField( null=True, blank=True , default="https://www.facebook.com/Sainikschoolentranceexamcoaching/")
    instagram_link = models.CharField( null=True, blank=True , default="https://www.instagram.com/onlinesainikschoolcoaching/")
    youtube_link = models.CharField(max_length=500, null=True, blank=True , default="https://www.youtube.com/@rdajaipur")
    meta_title = models.CharField(  null=True, blank=True , default="Top Coaching for Sainik School location, RMS, and RIMC Entrance Exams location")
    meta_description = models.CharField( null=True, blank=True , default="sainik school coaching location, rashtriya military school coaching location, rms entrance exam coaching, rimc coaching, military school entrance exam coaching, sainik school entrance exam coaching, rashtriya military school entrance exam, rimc entrance exam coaching location")
    latitude   = models.CharField( null=True, blank=True)
    logitude  = models.CharField( null=True, blank=True)
    pincode = models.CharField( null=True, blank=True)
    def save(self, *args, **kwargs):
        # Only replace if `title` exists and is not None
        if self.title:
            self.description = self.description.replace("location", self.title)
            self.short_description = self.short_description.replace("location", self.title)
            self.meta_keyword = self.meta_keyword.replace("location", self.title)
            self.meta_title = self.meta_title.replace("location", self.title)
            self.meta_description = self.meta_description.replace("location", self.title)

        # Debug print statements
        print(f"Saving locality: {self.title}")
        print(f"Description: {self.description}")
        
        # Save the instance
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
    
class Localities(models.Model):
    city = models.ForeignKey(Cities, on_delete=models.CASCADE , null= True , blank=True, related_name='localities')
    title = models.CharField(max_length=250 , null= True , blank=True)
    description = models.TextField(max_length=500, null=True, blank=True ,default="Top Coaching for Sainik School location , RMS, and RIMC Entrance Exams Join the best coaching center for Sainik School location , Rashtriya Military School (RMS), and RIMC entrance exams location. Achieve your dream of joining prestigious military schools with our expert guidance and proven success strategies location.")
    short_description = models.TextField( null=True, blank=True  , default="Expert coaching for Sainik School location, Rashtriya Military School (RMS), and RIMC entrance exams location. Comprehensive preparation, experienced faculty, and proven results location.")
    Image = models.ImageField(upload_to='covers/', blank=True, null=True)
    image_alt = models.CharField( null=True, blank=True)
    meta_keyword = models.TextField(null=True, blank=True , default="sainik school coaching location , rashtriya military school coaching location, rms entrance exam coaching, rimc coaching, military school entrance exam coaching, sainik school entrance exam coaching, rashtriya military school entrance exam, rimc entrance exam coaching, military school coaching location, rms coaching, sainik school coaching, rimc coaching, military entrance exam preparation location")
    contact_number = models.CharField(max_length=100, null=True, blank=True , default="8769422006")
    whatsapp_number = models.CharField(max_length=100 , null=True,  blank=True ,default="8278640248")
    facebook_link = models.CharField( null=True, blank=True , default="https://www.facebook.com/Sainikschoolentranceexamcoaching/")
    instagram_link = models.CharField( null=True, blank=True , default="https://www.instagram.com/onlinesainikschoolcoaching/")
    youtube_link = models.CharField(max_length=500, null=True, blank=True , default="https://www.youtube.com/@rdajaipur")
    meta_title = models.CharField( null=True, blank=True  , default="Top Coaching for Sainik School location, RMS, and RIMC Entrance Exams location")
    meta_description = models.CharField( null=True, blank=True , default="sainik school coaching location, rashtriya military school coaching location, rms entrance exam coaching, rimc coaching, military school entrance exam coaching, sainik school entrance exam coaching, rashtriya military school entrance exam, rimc entrance exam coaching location")
    latitude   = models.CharField( null=True, blank=True)
    logitude  = models.CharField( null=True, blank=True)
    pincode = models.CharField( null=True, blank=True)
    def __str__(self):
        return self.title
   
