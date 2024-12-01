from django.shortcuts import render
# myapp/views.py
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
# Create your views here.
class StateLimitedAPIView(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateLimitedSerializer
class CitiesAPIView(ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesFullSerializer

class StateFullAPIView(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateFullSerializer

class LocalitiesAPIView(ModelViewSet):
    queryset = Localities.objects.all()
    serializer_class = LocalitiesSerializer 