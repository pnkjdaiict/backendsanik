import django_filters
from .models import *
from states.models import *

class CityFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive contains
    
    state = django_filters.ModelMultipleChoiceFilter(queryset=State.objects.all())  # For filtering by states
  
    class Meta:
        model = Cities
        fields = ['title',  'state' ]
class LocalityFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive contains
    
    state = django_filters.ModelMultipleChoiceFilter(queryset=State.objects.all())  # For filtering by states
  
    class Meta:
        model = Localities
        fields = ['title',  'state' ,'city' ]