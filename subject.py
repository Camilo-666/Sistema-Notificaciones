# subject.py
from typing import List
from observer import Observer

class Subject:
    def attach(self, observer: Observer):
        raise NotImplementedError

    def detach(self, observer: Observer):
        raise NotImplementedError

    def notify_observers(self, message: str):
        raise NotImplementedError


class NotificationTopic(Subject):
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self, message: str):
        for observer in self._observers:
            observer.update(message)

    # helper
    def publish(self, message: str):
        print(f"\n📢 Publicando mensaje: {message}")
        self.notify_observers(message)
