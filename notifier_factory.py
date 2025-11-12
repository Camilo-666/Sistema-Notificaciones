# notifier_factory.py
from notifiers import EmailNotifier, SmsNotifier, PushNotifier

class NotifierFactory:
    def create_notifier(self):
        raise NotImplementedError


class EmailNotifierFactory(NotifierFactory):
    def create_notifier(self):
        return EmailNotifier()


class SmsNotifierFactory(NotifierFactory):
    def create_notifier(self):
        return SmsNotifier()


class PushNotifierFactory(NotifierFactory):
    def create_notifier(self):
        return PushNotifier()
