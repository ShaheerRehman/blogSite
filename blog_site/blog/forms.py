from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('author', 'title', 'text')
        
        widgets = {
            'author': forms.Select(attrs={
                'class': 'form-select'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Blog Title'
            }),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea form-control'}),
        }
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('author', 'text')
        
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Author Name'
            }),
            'text': forms.Textarea(attrs={
                'class': 'editable medium-editor-textarea form-control'
            }),
        }