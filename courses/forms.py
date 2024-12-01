from django import forms
from .models import *

class CourseForm(forms.ModelForm):
    # SubCourses = forms.ModelMultipleChoiceField(
    #     queryset=SubCourse.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    #      )
    short_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 50  # Number of visible columns
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
            'cols': 50  # Number of visible columns
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
            'cols': 50  # Number of visible columns
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

