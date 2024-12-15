
from rest_framework import serializers
from .models import *
class newsDataSerializer(serializers.ModelSerializer):
    class Meta :
        model = news
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
class newsHomepageSerializer(serializers.ModelSerializer):
    class Meta:
        model = news
        fields = ['title', 'short_description', 'image', 'author',]