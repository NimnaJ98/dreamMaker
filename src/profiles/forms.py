from django import forms
from django.forms import fields
from .models import Profile

#create a form based on profile model. 
class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name','last_name', 'bio', 'avatar', 'address', 'education', 'qualifications', 'experience')