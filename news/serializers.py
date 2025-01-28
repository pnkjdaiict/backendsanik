
from rest_framework import serializers
from .models import *
class NewsSerializer(serializers.ModelSerializer):
    class Meta :
        model = News
        fields = [
            'id',
            'title',
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
class NewsHomepageSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'short_description', 'image', 'author',]
class NewsSlugSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'short_description', 'image', 'author',]