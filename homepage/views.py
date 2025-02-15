# myapp/views.py
from rest_framework.viewsets import ModelViewSet
from .models import Banner
from .serializers import * 
from .filters import * 
from django_filters.rest_framework import DjangoFilterBackend
class SEOViewSet(ModelViewSet):
    
    queryset = SEO.objects.all()
    serializer_class = SEOSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']  # Allow GET, POST, PATCH, DELETE (optional)

class HomepageViewSet(ModelViewSet):
    queryset = Banner.objects.all()  # Get all Banner objects
    serializer_class = BannerSerializer  # Use BannerSerializer for serialization
    http_method_names = ['get', 'post', 'patch', 'delete']  # Allow GET, POST, PATCH, DELETE (optional)

class HomepageTopScrollViewSet(ModelViewSet):
    queryset = TopScroller.objects.all()
    serializer_class= TopScrollerSerializer
    http_method_names = ['get','post','delete' ,'patch']

class HomePageImagesViewSet(ModelViewSet):
    queryset = HomePageImages.objects.all()
    serializer_class = HomePageImagesSerializer
    http_method_names = ['get','post','delete' ,'patch']

class LineScrollBarViewSet(ModelViewSet):
    queryset = LineScrollBar.objects.all()
    serializer_class = LineScrollBarSerializer
    http_method_names=['get','post', 'delete','patch']

class EnquieryFormViewSet(ModelViewSet):
    queryset = EnquiryForm.objects.all()
    serializer_class= EnquieryFormSerializer
    http_method_names = ['get', 'post', 'delete','patch']

class FAQViewSet(ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FAQFilter
    http_method_names = ['get', 'post', 'delete','patch']
class HomepageContentView(ModelViewSet):
    queryset = HomepageContent.objects.all()
    serializer_class= HomepageContentSerializer
    http_method_names = ['get', 'post', 'delete','patch']

