from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
# Create your views here.
class BlogPagination(PageNumberPagination):
    page_size = 5  # Default number of items per page
    page_size_query_param = 'limit'  # Allow clients to set custom limit
    max_page_size = 100  # Upper limit for page size

class BlogsViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class= BlogSerializer
    http_method_names = ['get', 'post', 'delete','patch']

class BlogHomepageViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.order_by('-created_at')
    serializer_class = BlogHomepageSerializer
    pagination_class = BlogPagination
    http_method_names = ['get', 'post', 'delete','patch']
...
