from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    # Customize the title field
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter blog title',
        })
    )
    
    # Customize the short description field
    short_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a short description',
            'rows': 3,
        })
    )
    
    # Customize the slug field
    slug_field = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter slug (leave blank to auto-generate)',
        }),
        required=False
    )
    
    # Customize the description field
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter full blog content',
            'rows': 10,
        })
    )
    
    # Customize the author field
    author = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter author name',
        })
    )
    
    # Customize the status field
    status = forms.ChoiceField(
        choices=Blog._meta.get_field('status').choices,
        widget=forms.Select(attrs={
            'class': 'form-select',
        })
    )
    
    # Customize the image field
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
        }),
        required=False
    )
    
    # Customize the meta fields
    meta_title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter meta title',
        }),
        required=False
    )
    
    meta_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter meta description',
            'rows': 3,
        }),
        required=False
    )
    
    meta_keywords = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter meta keywords, separated by commas',
        }),
        required=False
    )
    
    class Meta:
        model = Blog
        fields = '__all__'  # Include all fields in the form
