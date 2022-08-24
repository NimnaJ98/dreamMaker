from django import forms
from .models import Audition, Star


class AuditionForm(forms.ModelForm):
    name = forms.CharField(widget=forms.Textarea(attrs={'rows':1}))
    qualifications = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    requirements = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    additional_info = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))

    class Meta:
        model = Audition
        fields = ('name', 'type','image', 'qualifications', 'requirements', 'additional_info', 'due_date')
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }