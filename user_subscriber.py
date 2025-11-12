# user_subscriber.py
from observer import Observer

class UserSubscriber(Observer):
    def __init__(self, name: str, notifier_factory):
        self.name = name
        self.notifier = notifier_factory.create_notifier()

    def update(self, message: str):
        self.notifier.send(self.name, message)
