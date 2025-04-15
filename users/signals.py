from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import EmailMultiAlternatives
from django.conf import settings  # Get the .env variables for sending emails.


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

        subject = 'Welcome to DevSearch!'
        from_email = settings.EMAIL_HOST_USER
        recipient_email = profile.email
        text_content = f"Thank you, {profile.name} for signing up. We are glad you're here."
        html_content = f"""
                <html>
                  <head></head>
                  <body>
                    <p>
                      Thank you, {profile.name} for signing up. We are glad you're here.
                    </p>
                  </body>
                </html>
                """
        msg = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=from_email,
            to=[recipient_email]
        )
        msg.attach_alternative(
            content=html_content,
            mimetype="text/html"
        )
        msg.send()


def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if not created:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


# NOT USED!!!!
# See comment on 'post_delete' signal below.
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


# Demonstrates how to connect a signal to a function instead of using a decorator.
post_save.connect(receiver=create_profile, sender=User)
post_save.connect(receiver=update_user, sender=Profile)

# This signal was created by the instructor, but causes a circular logic issue.
# If an admin deletes a profile from the admin page, the function called here
# will also delete the user. However, if a user is deleted, the Profile model
# is set to 'on_delete=models.CASCADE' and will try to delete a Profile that no longer exists.
# post_delete.connect(receiver=delete_user, sender=Profile)