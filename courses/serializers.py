


from rest_framework import serializers
from .models import *
from states.models import *
from rest_framework import serializers
from .models import Image
from .serializers import *
class MultipleImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = multiple_images
        fields = ['id', 'title', 'imagess', 'image_alt', 'contact_number', 'meta_title', 'meta_description', 'meta_keyword']

class multi_descriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = multiple_descriptions
        fields = [
            'id', 
            'description',
            'course', 
        ]
class multi_titleSerializer(serializers.ModelSerializer):
    class Meta:
        model = multiple_title
        fields = [
            'id', 
            'title',
            'course', 
        ]
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
class LocalitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localities
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

# Serializer for seo Course Model
class CourseSeoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSeoData
        fields = [
            "meta_title",
            "meta_description",
            "meta_keywords",
            "og_title",
            "og_description",
            "og_image",
            "twitter_card",
        ]
# Serializer for Course Model
class CourseSeoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSeoData
        fields = [
            "meta_title",
            "meta_description",
            "meta_keywords",
            "og_title",
            "og_description",
            "og_image",
            "twitter_card",
        ]
# Serializer for Course Model

class CourseSerializer(serializers.ModelSerializer):
    multiple_title = multi_titleSerializer(many=True, read_only=True)
    multiple_description  = multi_descriptionSerializer(many=True, read_only=True)
    multiple_imagess = MultipleImagesSerializer(many=True, read_only=True)
    states = StateSerializer(many=True, read_only=True)
    cities = CitySerializer(many=True, read_only=True)
    localities = LocalitiesSerializer(many=True, read_only=True)
    sub_courses = SubCourseSerializer(many=True, read_only=True)
    coursesn = SubCourseSerializer(many=True, read_only=True)  # Use the related_name defined in the Course model
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'short_title',
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
            'images' ,
            'multiple_title',
            'multiple_imagess',
            'multiple_description' ,
       
        ]

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'title' ,'short_description', 'description', 'image', 'image_alt', 
                  'price' , 'meta_keyword', 'contact_number', 'facebook_link', 'instagram_link', 
                  'youtube_link', 'meta_title', 'meta_description']

class CityCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'slug_field',
            'short_title',
            'short_description',
            'slug_field',
            'description',
           
        ]
class StateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'slug_field',
            'short_title',
            'short_description',
            'description',
            'contact_number',
            'youtube_link',
            'facebook_link',
            'instagram_link' ,
      ]
    def validate_slug_field(self, value):
        if not value.islower():
            raise serializers.ValidationError("Slug field must be in lowercase.")
        return value


class CityWithCoursesSerializer(serializers.ModelSerializer):
    # Include the related courses for each city
    courses = CityCourseSerializer(many=True, read_only=True)
    class Meta:
        model = Cities
        fields = ['id', 'title', 'courses']   

class StateWithCoursesSerializer(serializers.ModelSerializer): 
    courses = StateCourseSerializer(many=True, read_only=True)
    class Meta:
        model = State
        fields = ['id', 'title', 'courses' , 'Image' ,'contact_number','image_alt','instagram_link','short_description','title']   

        