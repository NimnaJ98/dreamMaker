from django import forms
from django.forms import fields
from .models import Post, Comment

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    class Meta:
        model = Post
        fields = ('content','image', 'video')

class CommentModelForm(forms.ModelForm):
    body = forms.CharField(label='', 
                        widget=forms.TimeInput(attrs={'placeholder':'Add a comment...'}))
    class Meta:
        model = Comment
        fields = ('body',)
