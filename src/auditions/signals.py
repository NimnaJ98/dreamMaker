from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Participate


#whenever a user joins an audition, the user will be included in the directors participant list.
@receiver(post_save, sender=Participate)
def post_save_add_to_participant(sender, instance, created, **kwargs):
    participant_ =instance.participant
    audition_ = instance.audition
    if instance.status == 'requested':
        audition_.participants.add(participant_.user)
        participant_.save()
        audition_.save()

#Remove a friend from the friends list
@receiver(pre_delete, sender=Participate)
def pre_delete_remove_friend(sender, instance, **kwargs):
    participant = instance.participant
    audition = instance.audition
    audition.participants.remove(participant.user)
    participant.save()
    audition.save()