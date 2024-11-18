 
from django import forms
from .models import EnquiryForm  # Assuming your EnquiryForm model is in the same directory
from courses.models import Course  # Assuming the Course model is in the 'courses' app

class EnqForm(forms.ModelForm):
    # Create a Many-to-Many relationship field for courses
    type = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),  # Query all courses
        widget=forms.CheckboxSelectMultiple,  # Display as checkboxes
        required=False  # Optional, if you want to make it optional
    )

    class Meta:
        model = EnquiryForm  # The model we're working with is EnquiryForm
        fields = ['type', 'name', 'email', 'phone', 'message']  # Include all relevant fields





