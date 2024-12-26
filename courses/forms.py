from django import forms
from .models import *
class multititleForm(forms.ModelForm):
   
    title = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 2,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )
    class Meta:
        model = multiple_title
        fields = '__all__'
from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    title  = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 2,
            'cols': 100
        }),
        required=False
    )
    image_alt = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 2,
            'cols': 100
        }),
        required=False
    )
    meta_keyword = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,
            'cols': 100
        }),
        required=False
    )
    contact_number = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 2,
            'cols': 50
        }),
        required=False
    )
    youtube_link = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 2,
            'cols': 100
        }),
        required=False
    )
    facebook_link = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 2,
            'cols': 100
        }),
        required=False
    )
    instagram_link = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 2,
            'cols': 100
        }),
        required=False
    )
    meta_title = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 2,
            'cols': 100
        }),
        required=False
    )
    meta_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,
            'cols': 100
        }),
        required=False
    )

    class Meta:
        model = Image
        fields = '__all__'  # Include all fields in the form

class CourseForm(forms.ModelForm):
   
    title = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )
    short_title = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )
    image_alt = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )
    course_code= forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )
    slug_field=forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )
    youtube_link = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )
    facebook_link = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )
    instagram_link = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )
    meta_title = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )
    meta_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )
    short_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )     
    states = forms.ModelMultipleChoiceField(
        queryset=State.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    cities = forms.ModelMultipleChoiceField(
        queryset=Cities.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )  
    localities = forms.ModelMultipleChoiceField(
        queryset=Localities.objects.all(),
        widget=forms.CheckboxSelectMultiple
    ) 
    class Meta:
        model = Course
        fields = '__all__'

class SubCategoriesForm(forms.ModelForm):
    subcourse = forms.ModelMultipleChoiceField(
        queryset=SubCourse.objects.all(),
        widget=forms.CheckboxSelectMultiple
         )
    short_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
        )
    
    # states = forms.ModelMultipleChoiceField(
    #     queryset=State.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )
    # cities = forms.ModelMultipleChoiceField(
    #     queryset=Cities.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )  

    class Meta:
        model = SubCourse
        fields = '__all__'

class SubCourseForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple
         )
    short_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
        )
    title = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 100  # Number of visible columns
        }),
     )
    slug_field=forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )
    youtube_link = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )
    facebook_link = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )
    instagram_link = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )
    meta_title = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )
    meta_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )
    short_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )
    
    
    states = forms.ModelMultipleChoiceField(
        queryset=State.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    cities = forms.ModelMultipleChoiceField(
        queryset=Cities.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )  
    
    # states = forms.ModelMultipleChoiceField(
    #     queryset=State.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )
    # cities = forms.ModelMultipleChoiceField(
    #     queryset=Cities.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )  

    class Meta:
        model = SubCourse
        fields = '__all__'


class CourseSeoDataForm(forms.ModelForm):
    meta_title = forms.CharField(
        widget=forms.Textarea( attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
        required=False
    )

    meta_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,
            'cols': 150
        }),
        required=False
    )

    meta_keywords = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,
            'cols': 150
        }),
        required=False
    )

    og_title = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,
            'cols': 150
        }),
        required=False
    )

    og_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,
            'cols': 150
        }),
        required=False
    )

    

    twitter_card = forms.ChoiceField(
        choices=[("summary", "Summary"), ("summary_large_image", "Summary Large Image")],
        required=False
    )

    class Meta:
        model = CourseSeoData
        fields = '__all__'