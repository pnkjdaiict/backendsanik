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
from django.db.models import Prefetch
from django.http import JsonResponse
from .models import *
from rest_framework.pagination import PageNumberPagination

class CitiesPagination(PageNumberPagination):
    page_size = 20  # Default page size (can be overridden by query params)
    page_size_query_param = 'limit'  # Allows you to pass 'limit' as query param to adjust page size
    max_page_size = 100  # Max limit for page size


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
        
class HomepageCourseListAPIView(ModelViewSet):
    queryset = Course.objects.prefetch_related('coursesn').all()  # Prefetch related sub-courses
    # queryset = Course.objects.all()
    serializer_class = HomeCourseSerializer
    # http_method_names = ['get', 'post', 'patch', 'delete']  # Restrict allowed methods
   
class HomepageFeatureCourseListAPIView(ModelViewSet):
    queryset = Course.objects.prefetch_related('coursesn').all()  # Prefetch related sub-courses
    # queryset = Course.objects.all()
    serializer_class = HomeFeatureCourseSerializer
    # http_method_names = ['get', 'post', 'patch', 'delete']  # Restrict allowed methods
   

    
class SingleCourseListAPIView(ModelViewSet):
    queryset = Course.objects.prefetch_related('coursesn', ).all()  # Prefetch related sub-courses
    # queryset = Course.objects.all()
    serializer_class = SingleCourseSerializer
    # http_method_names = ['get', 'post', 'patch', 'delete']  # Restrict allowed methods
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_class = CourseFilter  # Specify the filter class
    
    def perform_create(self, serializer):
       
        if not serializer.validated_data.get('slug'):
            serializer.save(slug_field=slugify(serializer.validated_data['title']))
        else:
            serializer.save()
        def perform_create(self, serializer):
         if not serializer.validated_data.get('slug'):
            serializer.save(slug_field=slugify(serializer.validated_data['title']))
         else:
            serializer.save()

    def perform_update(self, serializer):
        # Save the course instance
        course = serializer.save()
        course.save()  # Save again to ensure changes are persisted


class CourseListAPIView(ModelViewSet):
    queryset = Course.objects.prefetch_related('coursesn', 'cities').all()  # Prefetch related sub-courses
    # queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # http_method_names = ['get', 'post', 'patch', 'delete']  # Restrict allowed methods
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_class = CourseFilter  # Specify the filter class
    
    def perform_create(self, serializer):
       
        if not serializer.validated_data.get('slug'):
            serializer.save(slug_field=slugify(serializer.validated_data['title']))
        else:
            serializer.save()
        def perform_create(self, serializer):
         if not serializer.validated_data.get('slug'):
            serializer.save(slug_field=slugify(serializer.validated_data['title']))
         else:
            serializer.save()

    def perform_update(self, serializer):
        # Save the course instance
        course = serializer.save()
        course.save()  # Save again to ensure changes are persisted



class CourseslugAPIView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseslugSerializer 
    http_method_names = ['get', 'post', 'patch', 'delete']  # Allow GET, POST, PATCH, DELETE (optional)

class CourseHeaderslugAPIView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseHeaderSerializer 
    http_method_names = ['get', 'post', 'patch', 'delete']  # Allow GET, POST, PATCH, DELETE (optional)
         
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
    serializer_class = CityWithCoursesSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']  # Optional: limit allowed HTTP methods
    # pagination_class =CitiesPagination

    def get_queryset(self):
     return Cities.objects.prefetch_related(
        Prefetch(
            'courses',
            queryset=Course.objects.only('slug_field', 'short_title')  # Fetch only required fields
        )
    ).all()
    
class StatesWithCoursesView(ModelViewSet):
        queryset = State.objects.all()
        serializer_class = StateWithCoursesSerializer 
        http_method_names = ['get', 'post', 'patch', 'delete']  # Allow GET, POST, PATCH, DELETE (optional)
class CourseListView(ModelViewSet):
        queryset = SubCategory.objects.all()
        serializer_class = SubCategorySerializer 
        http_method_names = ['get', 'post', 'patch', 'delete']  # Allow GET, POST, PATCH, DELETE (optional)
class CourseSeoDataViewSet(ModelViewSet):
    queryset = CourseSeoData.objects.all()
    serializer_class = CourseSeoDataSerializer
    http_method_names = ['get', 'post', 'patch', 'delete'] 
