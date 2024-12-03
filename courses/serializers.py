from rest_framework import serializers
from .models import *
from states.models import Cities
from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id', 
            'course', 
            'image', 
            'image_alt', 
            'meta_keyword', 
            'contact_number', 
            'youtube_link', 
            'facebook_link', 
            'instagram_link', 
            'meta_title', 
            'meta_description'
        ]
        extra_kwargs = {
            'course': {'write_only': True},  # Optionally hide course in the response
        }

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'  # Include all fields or specify specific fields

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'  # Include all fields or specify specific fields

# Serializer for SubCourse Model

class SubCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubCategory
        fields = ['id', 'title', 'short_description', 'description', 'image', 'image_alt', 
                  'price', 'meta_keyword', 'contact_number', 'facebook_link', 'instagram_link', 
                  'youtube_link', 'meta_title', 'meta_description']

class SubCourseSerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)   # Nested serializer for subcategories
    
    class Meta:
        model = SubCourse
        fields = [
            'id',
            'title',
            'slug_field',
            'short_description',
            'description',
            'image',
            'image_alt',
            'course_code',
            'courses',  
            'subcategories',
            'price',
            'meta_keyword',
            'contact_number',
            'facebook_link',
            'instagram_link',
            'youtube_link',
            'meta_title',
            'meta_description',
        ]


# Serializer for Course Model
class CourseSerializer(serializers.ModelSerializer):
    # Use SubCourseSerializer to serialize related sub_courses
    # SubCourses = SubCourseSerializer(many=True, read_only=True)
    states = StateSerializer(many=True, read_only=True)
    cities = CitySerializer(many=True, read_only=True)

    sub_courses = SubCourseSerializer(many=True, read_only=True)
    coursesn = SubCourseSerializer(many=True, read_only=True)  # Use the related_name defined in the Course model
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'short_description',
            'slug_field',
            'description',
            'image', 
            'image_alt', 
            'states', 
            'cities',
            'localities', 
            'sub_courses',
            'coursesn',
            'course_code', 
            'meta_keyword',
            'contact_number',
            'youtube_link',
            'facebook_link',
            'instagram_link',
            'meta_title',
            'meta_description',
            'images'
        ]

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'title' ,'short_description', 'description', 'image', 'image_alt', 
                  'price' , 'meta_keyword', 'contact_number', 'facebook_link', 'instagram_link', 
                  'youtube_link', 'meta_title', 'meta_description']

class CityWithCoursesSerializer(serializers.ModelSerializer):
    # Include the related courses for each city
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Cities
        fields = ['id', 'title', 'courses']   