from django.contrib import admin
from .models import Audition, AuditionType, Star, Participant

# Register your models here.

admin.site.register(Audition)
admin.site.register(AuditionType)
admin.site.register(Star)
admin.site.register(Participant)
