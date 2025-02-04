import django_filters
from .models import FAQ, Course

class FAQFilter(django_filters.FilterSet):
    course = django_filters.ModelChoiceFilter(
        queryset=Course.objects.all(),  # Fetch all courses
        field_name="course",
        label="Course Name"  # Label for the filter in the UI
    )

    class Meta:
        model = FAQ
        fields = ['course']

