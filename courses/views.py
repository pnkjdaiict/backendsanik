from django.shortcuts import render
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from .models import Course, SubCourse
from states.models import *
from .serializers import *
 
# View to get all courses
class CourseListAPIView(ModelViewSet):
    
        queryset = Course.objects.all()
        serializer_class = CourseSerializer
        http_method_names = ['get', 'post', 'patch', 'delete']  # Allow GET, POST, PATCH, DELETE (optional)


# View to get all sub-courses for a given course
class SubCourseListAPIView(ModelViewSet):
        
        queryset = SubCourse.objects.all()
        serializer_class = SubCourseSerializer
        http_method_names = ['get', 'post', 'patch', 'delete']  # Allow GET, POST, PATCH, DELETE (optional)


class CitiesWithCoursesView(ModelViewSet):
        queryset = Cities.objects.all()
        serializer_class = CityWithCoursesSerializer 
        http_method_names = ['get', 'post', 'patch', 'delete']  # Allow GET, POST, PATCH, DELETE (optional)
