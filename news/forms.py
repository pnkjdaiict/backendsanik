from django import forms
from .models import *

class NewsForm(forms.ModelForm):
    # SubCourses = forms.ModelMultipleChoiceField(
    #     queryset=SubCourse.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    #      )
    title = forms.CharField(
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
    author=forms.CharField(
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
    meta_keywords = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  # Number of visible rows
            'cols': 150  # Number of visible columns
        }),
     )
     
   
    
  