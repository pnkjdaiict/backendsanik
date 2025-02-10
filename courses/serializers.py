


from rest_framework import serializers
from .models import *
from states.models import * 
from .models import Image
from .serializers import *
from rest_framework.pagination import PageNumberPagination
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

 
class CitiesPagination(PageNumberPagination):
    page_size = 20  # Default page size (can be overridden by query params)
    page_size_query_param = 'limit'  # Allows you to pass 'limit' as query param to adjust page size
    max_page_size = 100  # Max limit for page size


# CitySerializer with state_object
class CitySerializer(serializers.ModelSerializer):
    # state_object = StateSerializer()
    # state_title = serializers.CharField(source='state.title', read_only=True)
    paginationclass = CitiesPagination
    class Meta:
        model = Cities
        fields = [
            'Image',
            'contact_number',
            'description',
            'facebook_link',
            'id',
            'image_alt',
            'instagram_link',
            'latitude',
            'logitude',
            'meta_description',
            'meta_keyword',
            'meta_title',
            'pincode',
            'short_description',
            'state',
            # 'state_title',
            'title',
            'whatsapp_number',
            'youtube_link',
            # 'state_object',  # Includes state details
        ]  # Include all fields or specify specific fields
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

class HomeCourseSerializer(serializers.ModelSerializer):
    # coursesn = SubCourseSerializer(many=True, read_only=True)  # Use the related_name defined in the Course model
    multiple_imagess = MultipleImagesSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = [
            'id',
            'title',             
            'short_description',
            'slug_field',
            # 'coursesn' ,
            'multiple_imagess',
        ]

    
class SingleCourseSerializer(serializers.ModelSerializer):
    multiple_title = multi_titleSerializer(many=True, read_only=True)
    multiple_description  = multi_descriptionSerializer(many=True, read_only=True)
    multiple_imagess = MultipleImagesSerializer(many=True, read_only=True)
    states = StateSerializer(many=True, read_only=True)
    state_ids = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all(),
        source='states',   
        many=True,
        write_only=True  
    )
    city_ids = serializers.PrimaryKeyRelatedField(
        queryset=Cities.objects.all(),
        source='cities',  # Maps to the `cities` field in the Course model
        many=True,
        write_only=True  
    )
    locality_ids = serializers.PrimaryKeyRelatedField(
        queryset=Localities.objects.all(),
        source='localities',   
        many=True,
        write_only=True   
    )
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
            'state_ids',
            'city_ids' ,  
            'locality_ids',  
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
   

class CourseSerializer(serializers.ModelSerializer):
    multiple_title = multi_titleSerializer(many=True, read_only=True)
    multiple_description  = multi_descriptionSerializer(many=True, read_only=True)
    multiple_imagess = MultipleImagesSerializer(many=True, read_only=True)
    states = StateSerializer(many=True, read_only=True)
    state_ids = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all(),
        source='states',   
        many=True,
        write_only=True  
    )
    city_ids = serializers.PrimaryKeyRelatedField(
        queryset=Cities.objects.all(),
        source='cities',  # Maps to the `cities` field in the Course model
        many=True,
        write_only=True  
    )
    locality_ids = serializers.PrimaryKeyRelatedField(
        queryset=Localities.objects.all(),
        source='localities',   
        many=True,
        write_only=True   
    )
    cities = serializers.SerializerMethodField()
    localities = serializers.SerializerMethodField()
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
            'state_ids',
            'city_ids' ,  
            'locality_ids',  
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
    def get_cities(self, obj):
        """
        Returns only the first 20 cities.
        """
        cities = obj.cities.all()[:20]  # Limits to 10 cities
        return CitySerializer(cities, many=True).data
    def get_localities(self, obj):
        """
        Returns only the first 20 cities.
        """
        localities = obj.localities.all()[:10]  # Limits to 10 localities
        return LocalitiesSerializer(localities, many=True).data


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
            # 'id',
            # 'title',
            # 'image',
            'slug_field',
            'short_title',
            # 'short_description',
            # 'slug_field',
            # 'description',
           
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
        fields = ['id', 'title', 'courses' ]   

class StateWithCoursesSerializer(serializers.ModelSerializer): 
    courses = StateCourseSerializer(many=True, read_only=True)
    class Meta:
        model = State
        fields = ['id', 'title', 'courses' , 'Image' ,'contact_number','image_alt','instagram_link','short_description','title']   

class CourseslugSerializer(serializers.ModelSerializer):
      class Meta:
        model = Course
        fields = [ 
            'id',
            'title' ,
            'short_title',
            'slug_field',
            'states'  , "cities" , "localities"
            ]
          