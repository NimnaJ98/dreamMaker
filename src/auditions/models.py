from django.db import models
from profiles.models import Profile

# Create your models here.
class AuditionType(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title

class Audition(models.Model):
    director = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='auditions')
    type = models.ForeignKey(AuditionType, related_name='auditions', on_delete=models.CASCADE)
    name = models.TextField()
    qualifications = models.TextField()
    requirements = models.TextField()
    additional_info = models.TextField()
    due_date = models.DateTimeField()

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return self.name

    
