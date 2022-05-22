from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import FileExtensionValidator
from profiles.models import Profile
# Create your models here.

class Audition(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='auditions', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    interested = models.ManyToManyField(Profile, blank=True, related_name='interests')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    organiser = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='auditions')

    def __str__(self):
        return str(self.content[:20])

    def num_interests(self):
        return self.interested.all().count()

    def num_eventcomments(self):
        return self.eventcomment_set.all().count()

    class Meta:
        ordering = ('-created',)

class EventComment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    audition = models.ForeignKey(Audition, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return str(self.pk)

INTEREST_CHOICES = (
    ('Interest', 'Interest'),
    ('Uninterest', 'Uninterest'),
)

class Interest(models.Model): 
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    audition = models.ForeignKey(Audition, on_delete=models.CASCADE)
    value = models.CharField(choices=INTEREST_CHOICES, max_length=10)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}-{self.audition}-{self.value}"