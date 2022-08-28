from django.db import models
from profiles.models import Profile
from django.core.validators import FileExtensionValidator

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
    image = models.ImageField(upload_to='auditions', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    qualifications = models.TextField()
    requirements = models.TextField()
    additional_info = models.TextField()
    due_date = models.DateTimeField()
    starred = models.ManyToManyField(Profile, blank=True, related_name='stars')
    participants = models.ManyToManyField(Profile, blank=True, related_name='participants')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.name

    def starred_profiles(self):
        return self.starred.all()

    def num_stars(self):
        return self.starred.all().count()

    
STAR_CHOICES = (
    ('Star', 'Star'),
    ('Unstar', 'Unstar'),
)

class Star(models.Model): 
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    audition = models.ForeignKey(Audition, on_delete=models.CASCADE)
    value = models.CharField(choices=STAR_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}-{self.audition}-{self.value}"


STATUS_CHOICES = (
    ('requested','requested'),
    ('accepted','accepted')
)

class ParticipateManager(models.Manager):
    def requests_received(self, audition):
        qs = Participate.objects.filter(audition=audition, status='requested')
        return qs 

class Participate(models.Model): 
    participant = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='participant')
    audition = models.ForeignKey(Audition, on_delete=models.CASCADE, related_name='audition')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    fullname = models.CharField(max_length=200, blank=True)
    age = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(default = 'avatar.png', upload_to = 'participants')
    education = models.CharField(max_length=200, blank=True)
    qualifications = models.CharField(max_length=200, blank=True)
    experience = models.CharField(max_length=200, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = ParticipateManager()



    def __str__(self):
        return f"{self.participant}-{self.audition}-{self.status}"