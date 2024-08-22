from django.apps import AppConfig
import logging

class UsersConfig(AppConfig):
    print("start")
    name = 'backend.users'

    def ready(self):
        print("start")
        import backend.users.signals.customerSignal
