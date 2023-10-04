from django import forms
from .models import BlogPost, Category, Tag
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'categories', 'tags', 'image']
        widgets = {
            'content': CKEditorWidget(),
        }
