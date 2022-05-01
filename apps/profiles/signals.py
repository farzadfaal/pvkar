from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.accounts.models import User

from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # if the user created for the first time and role is "contractor"
    if created and instance.role == User.Roles.contractor:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Check if a profile related to the user exists
    if instance.role == User.Roles.contractor:
        if not Profile.objects.filter(user=instance).exists():
            Profile.objects.create(user=instance)
