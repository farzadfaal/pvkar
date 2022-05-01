from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.accounts.models import User

from .models import Subscription


@receiver(post_save, sender=User)
def create_subscription(sender, instance, created, **kwargs):
    # if the user created for the first time and role is "contractor"
    if created:
        if instance.role == User.Roles.employer:
            Subscription.objects.create(user=instance, credit=25000)
        if instance.role == User.Roles.contractor:
            Subscription.objects.create(user=instance, credit=2000)
