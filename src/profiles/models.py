from distutils.command import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from .utils import get_randomCode
from django.template.defaultfilters import slugify

# Create your models here.

class Profile(models.Model):
    #to identify the logged in user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #profile data
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    bio = models.TextField(max_length=300, default="No bio...")
    email = models.EmailField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(default = 'avatar.png', upload_to = 'avatars')
    education = models.CharField(max_length=200, blank=True)
    qualifications = models.CharField(max_length=200, blank=True)
    experience = models.CharField(max_length=200, blank=True)

    #to get user's followers
    friends = models.ManyToManyField(User, blank=True, related_name='friends')

    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()

    #string representation
    def __str__(self):
        return f"{self.user.username}-{self.created.straftime('%d-%m-%y')}"

    #generate a random slug when there're 2 or more profiles with the same name
    def save(self, *args, **kwargs):
        sluExist = False
        if self.first_name and self.last_name:
            to_slug = slugify(str(self.first_name) + " " + str(self.last_name))
            sluExist = Profile.objects.filter(slug=to_slug).exists()
            while sluExist:
                to_slug = slugify(to_slug + " " + str(get_randomCode()))
                sluExist = Profile.objects.filter(slug=to_slug).exists()
        else:
            to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)

STATUS_CHOICES = (
    ('send','send'),
    ('accepted','accepted')
)


class Relationship(models.Model):
        sender = models.ForignKey(Profile, on_delete=models.CASCADE, related_name='sender')
        receiver = models.ForignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
        status = models.CharField(max_length=8, choices=STATUS_CHOICES)
        updated = models.DateTimeField(auto_now=True)
        created = models.DateTimeField(auto_now_add=True)

        def _str_(self):
            return f"{self.sender}-{self.receiver}-{self.status}"
             