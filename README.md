# django-devsearch

Work in progress

A course project introducing the basics of Django. UIkit and static elements were provided by the course.

## TODOs:
- ~~Welcome email.~~
  - While this is technically working using send_mail from django.core.mail. It's getting flagged as spam.
    Try using an EmailMessage object instead. https://docs.djangoproject.com/en/5.0/topics/email/#the-emailmessage-class
  - Alternatively, use smtplib, MIMEText, and MIMEMultipart. I believe I may have used this before to avoid scripted 
    emails from getting marked as spam. See contact route in: 
    https://github.com/ArieKnoester/upgraded-flask-jinja-blog-exercise/blob/main/main.py
- Password reset.
- ~~Implement user messages and inbox.~~
- ~~Fix back buttons on some forms which are not going back to the correct page.~~
  - ~~Add Project back button goes to all-projects instead of users account page.~~
  - ~~Create message back button goes to account page instead of profile page of message recipient.~~