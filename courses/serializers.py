from rest_framework import serializers
from .models import *
from states.models import Cities

class SubCourseSerializer(serializers.ModelSerializer):
    # subcategories = SubCategorySerializer(many=True, read_only=True)  # Nested serializer for subcategories
    course = serializers.StringRelatedField(many=True)  
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
            # 'subcategories', 
            'price',
            'course',
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
    SubCourse = SubCourseSerializer(many=True, read_only=True) 
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
            'SubCourse',
            'course_code', 
            'meta_keyword',
            'contact_number',
            'youtube_link',
            'facebook_link',
            'instagram_link',
            'meta_title',
            'meta_description',
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

# Serializer for SubCourse Model
class SubCategorySerializer(serializers.ModelSerializer):
    subcourses = serializers.StringRelatedField(many=True)    # Adjust this line
    class Meta:
        model = SubCategory
        fields = ['id', 'title', 'short_description', 'description', 'image', 'image_alt', 
                  'price', 'meta_keyword', 'contact_number', 'facebook_link', 'instagram_link','youtube_link', 'meta_title', 'meta_description']
