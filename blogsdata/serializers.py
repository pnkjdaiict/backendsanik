
from rest_framework import serializers
from .models import *
class BlogDataSerializer(serializers.ModelSerializer):
    class Meta :
        model = Blog
        fields = [
            'id',
            'title',
            'slug_field',
            'short_description',
            'description',
            'author',
            'created_at',
            'updated_at',
            'status',
            'image',  
            'meta_title',
            'meta_description',
            'meta_keywords',
        ]
class BlogHomepageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [ 'id',
            'title',
            'slug_field',
            
            'author',
            
            'image',  
           ]
            

class BlogSlugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title' , 'slug_field' , ]