# blog/filters.py
import django_filters
from .models import Blog

class BlogFilter(django_filters.FilterSet):
    # Create filters for fields you want to filter by
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
    
    class Meta:
        model = Blog
        fields = ['title', 'author', 'status', 'created_at']

