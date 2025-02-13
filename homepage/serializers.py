from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from rest_framework.views import APIView
class SEOSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEO
        fields = [
    'title'  ,
    'homepagetitle',
    'logo',
    'description'  ,
    'keywords' , 
    'canonical_url'  ,
    'og_title'  ,
    'og_description' ,
    'keywords',
    'og_image'  ,
    'og_url'  ,
    'twitter_card'   ,
    'contact_number', 
    'address' ,
    'email' ,
    'scripts' ,
    'whatsapp_number' ,
    'location' 
        ]
    def validate_keywords(self, value):
        """Ensure meta_keyword is stored as a comma-separated string."""
        if isinstance(value, list):
            return ','.join(value)
        return value
   
    def to_representation(self, instance):
        """Modify the output representation (e.g., parse meta_keywords)."""
        data = super().to_representation(instance)
        if instance.keywords:
            data['keyword'] = instance.get_keywords()
        return data

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = [
            'id', 
            'Image', 
            'description', 
            'meta_title', 
            'meta_description', 
            'image_alt', 
            'meta_keyword', 
            'contact_number', 
            'facebook_link', 
            'instagram_link', 
            'title'
        ]

    def validate_meta_keywords(self, value):
        """Ensure meta_keyword is stored as a comma-separated string."""
        if isinstance(value, list):
            return ','.join(value)
        return value
   
    def to_representation(self, instance):
        """Modify the output representation (e.g., parse meta_keywords)."""
        data = super().to_representation(instance)
        if instance.meta_keyword:
            data['meta_keyword'] = instance.get_meta_keywords()
        return data

class TopScrollerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopScroller
        fields = [
            'Image',
            'image_alt',
            'description',
            'title',
        ]

class HomePageImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageImages
        fields = [
            'id',
            'Image',
            'description',
            'image_alt',
            'meta_keyword',
            'contact_number',
            'facebook_link',
            'instagram_link',
            'youtube_link',
            'title'
        ]

class LineScrollBarSerializer(serializers.ModelSerializer):
    class Meta :
        model =LineScrollBar
        fields = [
            'title',
            'link'
        ]
class EnquieryFormSerializer(serializers.ModelSerializer):
    class Meta :
        model = EnquiryForm
        fields = [
            'type' ,
            'name' ,
            'phone',
            'email',
            'message', 
            'cities' ,
            'states',
            'created_at'        
        ]
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id',  'course' ,'question', 'answer']

class HomepageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomepageContent
        fields = [ 
            'details', 
        ]