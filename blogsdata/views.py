from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .filter import * 
from django_filters.rest_framework import DjangoFilterBackend
class BlogsDataViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class= BlogDataSerializer
    http_method_names = ['get', 'post', 'delete','patch']
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_class = BlogFilter  # Specify the filter class

class BlogSlugViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class= BlogSlugSerializer
    http_method_names = ['get', 'post', 'delete','patch']
    
   