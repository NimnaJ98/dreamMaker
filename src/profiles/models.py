from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from .utils import get_random_code
from django.template.defaultfilters import default, slugify
from django.db.models import Q

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

    #generate a random slug when there're 2 or more profiles with the same first name
    __initial_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial_name = self.first_name

    def save(self, *args, **kwargs):
        ex =False
        to_slug = self.slug
        if self.first_name != self.__initial_name or self.slug=="":
            if self.first_name:
                to_slug = slugify(str(self.first_name))
                ex = Profile.objects.filter(slug = to_slug).exists()
                while ex:
                    to_slug = slugify(to_slug+" "+ str(get_random_code()))
                    ex = Profile.objects.filter(slug = to_slug).exists()
            else:
                to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)


STATUS_CHOICES = (
    ('send','send'),
    ('accepted','accepted')
)

class RelationshipManager(models.Manager):
    def invitations_received(self, receiver):
        qs = Relationship.objects.filter(receiver=receiver, status='send')
        return qs 


class Relationship(models.Model):
    
    #everytime a particular profile is deleted, the relationship will also be deleted. 
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')

    #to determine the status of the choice. whether it's a sent invitation or an invitation accepted
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = RelationshipManager()



    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"
             