# notifiers.py
class Notifier:
    def send(self, recipient: str, message: str):
        raise NotImplementedError


class EmailNotifier(Notifier):
    def send(self, recipient: str, message: str):
        print(f"[EMAIL] to {recipient}: {message}")


class SmsNotifier(Notifier):
    def send(self, recipient: str, message: str):
        print(f"[SMS] to {recipient}: {message}")


class PushNotifier(Notifier):
    def send(self, recipient: str, message: str):
        print(f"[PUSH] to {recipient}: {message}")
