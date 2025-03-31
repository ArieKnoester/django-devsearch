from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # connects this 'users' app to 'signals.py'
    def ready(self):
        import users.signals