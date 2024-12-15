from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.utils.html import format_html

from .filter import * 
from django_filters.rest_framework import DjangoFilterBackend
class newsViewSet(viewsets.ModelViewSet):
    queryset = news.objects.all()
    serializer_class= newsDataSerializer
    http_method_names = ['get', 'post', 'delete','patch']
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_class = newsFilter  # Specify the filter class
   