from django import forms
from .models import Audition

class AuditionForm(forms.ModelForm):
    
    class Meta:
        model = Audition
        fields = ('name', 'type','image', 'qualifications', 'requirements', 'additional_info', 'due_date')