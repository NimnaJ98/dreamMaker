from django.contrib import admin
from .models import Audition, AuditionType

# Register your models here.

admin.site.register(Audition)
admin.site.register(AuditionType)
