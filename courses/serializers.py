from rest_framework import serializers
from .models import Course, SubCourse
from states.models import Cities

# Serializer for SubCourse Model
class SubCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCourse
        fields = [
            'id',
            'title',
            'short_description',
            'description',
            'image',
            'image_alt',
            'course_code',
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
    SubCourses = SubCourseSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'short_description',
            'description',
            'image',
            'image_alt',
            'states',
            'cities',
            'course_code',
            'SubCourses',  # Nested serializer
            'meta_keyword',
            'contact_number',
            'youtube_link',
            'facebook_link',
            'instagram_link',
            'meta_title',
            'meta_description',
        ]

class CityWithCoursesSerializer(serializers.ModelSerializer):
    # Include the related courses for each city
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Cities
        fields = ['id', 'title', 'courses']  # Adjust fields based on your Cities model