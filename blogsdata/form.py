from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    title = forms.CharField(
       widget=forms.Textarea(attrs={
            'rows': 4,
            'cols': 100
        }),
    )
    slug_field = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the slug (auto-generated if left blank)',
              'rows': 4,
            'cols': 100
        }),
        required=False
    )
    short_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a short description',
            'rows': 3,
            'cols' : 100
        })
    )
  
     
    status = forms.ChoiceField(
        choices=Blog._meta.get_field('status').choices,
        widget=forms.Select(attrs={
            'class': 'form-select',
        })
    )
   
    meta_title = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the meta title for SEO',
              'rows': 4,
            'cols': 100
        }),
        required=False
    )
    meta_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the meta description for SEO',
            'rows': 4,
            'cols': 100
        }),
        required=False
    )
    meta_keywords = forms.CharField(
        widget=forms.Textarea(  attrs={
            'class': 'form-control',
            'placeholder': 'Enter meta keywords, separated by commas',
            'rows': 4,
            'cols': 100
        }),
        required=False
    )

    class Meta:
        model = Blog
        fields = '__all__'  # Include all fields in the form
