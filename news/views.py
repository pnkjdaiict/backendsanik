from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
# Create your views here.
class NewsPagination(PageNumberPagination):
    page_size = 5  # Default number of items per page
    page_size_query_param = 'limit'  # Allow clients to set custom limit
    max_page_size = 100  # Upper limit for page size

class NewssViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class= NewsSerializer
    http_method_names = ['get', 'post', 'delete','patch']

class NewsHomepageViewSet(viewsets.ModelViewSet):
    queryset = News.objects.order_by('-created_at')
    serializer_class = NewsHomepageSerializer
    pagination_class = NewsPagination
    http_method_names = ['get', 'post', 'delete','patch']
...
