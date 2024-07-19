from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        
        labels = {
            'title'   : 'Title',
            'content' : 'Content', 
            'image'   : 'Image',
        }
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content' :forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter content'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }