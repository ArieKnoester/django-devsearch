# django-devsearch

Work in progress

A course project introducing the basics of Django. UIkit and static elements were provided by the course.

## TODOs:
- ~~Password reset.~~
  - Need to figure out how to display form errors when using custom html templates for OOTB Django password reset views.
- ~~Welcome email.~~
  - ~~While this is technically working using send_mail from django.core.mail. It's getting flagged as spam.
    Try using an EmailMessage object instead. 
    https://docs.djangoproject.com/en/5.0/topics/email/#the-emailmessage-class~~
- ~~Implement user messages and inbox.~~
- ~~Fix back buttons on some forms which are not going back to the correct page.~~
  - ~~Add Project back button goes to all-projects instead of users account page.~~
  - ~~Create message back button goes to account page instead of profile page of message recipient.~~