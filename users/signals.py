from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


# Demonstrates how to connect a signal to a function using a decorator.
# Note that 'receiver' is imported.
# @receiver(signal=post_save, sender=Profile)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )


def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if not created:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


# Demonstrates how to connect a signal to a function instead of using a decorator.
post_save.connect(receiver=create_profile, sender=User)
post_save.connect(receiver=update_user, sender=Profile)
# post_delete.connect(receiver=delete_user, sender=Profile)