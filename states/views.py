from django.shortcuts import render
# myapp/views.py
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from .filters import * 
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from rest_framework.pagination import PageNumberPagination

class CitiesPagination(PageNumberPagination):
    page_size = 20  # Default page size (can be overridden by query params)
    page_size_query_param = 'limit'  # Allows you to pass 'limit' as query param to adjust page size
    max_page_size = 100  # Max limit for page size

class StateLimitedAPIView(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateLimitedSerializer
class CitiesAPIView(ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesFullSerializer
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_class = CityFilter  # Specify the filter class
    # pagination_class = CitiesPagination 
class CitiesAllAPIView(ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesFullSerializer
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_class = CityFilter  # Specify the filter class
   

class StateFullAPIView(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateFullSerializer

class LocalitiesAPIView(ModelViewSet):
    queryset = Localities.objects.all()
    serializer_class = LocalitiesSerializer 
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_class = LocalityFilter  # Specify the filter class
   
