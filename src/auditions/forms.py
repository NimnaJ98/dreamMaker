from django import forms
from .models import Audition

class AuditionModelForm(forms.ModelForm):
    name = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    qualifications = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    requirements = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    additional_info = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    class Meta:
        model = Audition
        fields = ('name', 'type', 'image', 'qualifications', 'requirements', 'additional_info', 'due_date')