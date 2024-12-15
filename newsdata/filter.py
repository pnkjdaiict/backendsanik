# news/filters.py
import django_filters
from .models import news

class newsFilter(django_filters.FilterSet):
    # Create filters for fields you want to filter by
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
    author = django_filters.CharFilter(lookup_expr='icontains', label='Author')
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
    slug_field = django_filters.CharFilter(lookup_expr='iexact') 
    created_at = django_filters.DateFromToRangeFilter(field_name='created_at', label='Created At')

    class Meta:
        model = news
        fields = ['title', 'author', 'status', 'created_at']

