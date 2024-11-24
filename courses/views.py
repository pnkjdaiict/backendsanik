from django.shortcuts import render
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from django.utils.text import slugify
from django import forms
from .models import Course, SubCourse
from states.models import *
from .serializers import *
from .filter import * 
from django_filters.rest_framework import DjangoFilterBackend
# View to get all courses
# views.py
from django.http import JsonResponse
from .models import *

def get_cities(request):
    state_id = request.GET.get('state_id')
    if state_id:
        cities = Cities.objects.filter(state_id=state_id).values('id', 'title')
        return JsonResponse(list(cities), safe=False)
    return JsonResponse([], safe=False)

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        if 'states' in self.data:
            state_id = self.data.get('states')
            self.fields['cities'].queryset = Cities.objects.filter(state_id=state_id)
        elif self.instance.pk:
            self.fields['cities'].queryset = self.instance.states.first().cities.all() if self.instance.states.exists() else Cities.objects.none()


class SubCategoryListView(ModelViewSet):
        queryset = SubCategory.objects.all()
        serializer_class = SubCategorySerializer
        
        http_method_names = ['get', 'post', 'patch', 'delete']  # Allow GET, POST, PATCH, DELETE (optional)
        


class CourseListAPIView(ModelViewSet):
   
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']  # Restrict allowed methods
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_class = CourseFilter  # Specify the filter class
    
    def perform_create(self, serializer):
       
        if not serializer.validated_data.get('slug'):
            serializer.save(slug_field=slugify(serializer.validated_data['title']))
        else:
            serializer.save()

    def perform_update(self, serializer):
         
        if not serializer.validated_data.get('slug'):
            serializer.save(slug_field=slugify(serializer.validated_data['title']))
        else:
            serializer.save()
# View to get all sub-courses for a given course
class SubCourseListAPIView(ModelViewSet):
        
        queryset = SubCourse.objects.all()
        serializer_class = SubCourseSerializer
        http_method_names = ['get', 'post', 'patch', 'delete']  # Allow GET, POST, PATCH, DELETE (optional)
        filter_backends = [DjangoFilterBackend]  # Enable filtering
        filterset_class = SubcourseFilter  # Specify the filter class
    
        def perform_create(self, serializer):
       
         if not serializer.validated_data.get('slug'):
            serializer.save(slug_field=slugify(serializer.validated_data['title']))
         else:
            serializer.save()

        def perform_update(self, serializer):
         
         if not serializer.validated_data.get('slug'):
            serializer.save(slug_field=slugify(serializer.validated_data['title']))
         else:
            serializer.save()

class CitiesWithCoursesView(ModelViewSet):
        queryset = Cities.objects.all()
        serializer_class = CityWithCoursesSerializer 
        http_method_names = ['get', 'post', 'patch', 'delete']  # Allow GET, POST, PATCH, DELETE (optional)
class CourseListView(ModelViewSet):
        queryset = SubCategory.objects.all()
        serializer_class = SubCategorySerializer 
        http_method_names = ['get', 'post', 'patch', 'delete']  # Allow GET, POST, PATCH, DELETE (optional)
   