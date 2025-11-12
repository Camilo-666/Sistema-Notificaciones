# main.py
from subject import NotificationTopic
from user_subscriber import UserSubscriber
from notifier_factory import EmailNotifierFactory, SmsNotifierFactory, PushNotifierFactory


def main():
    # Crear el tema (Subject)
    topic = NotificationTopic()

    # Crear observadores 
    ana = UserSubscriber("Ana", EmailNotifierFactory())
    luis = UserSubscriber("Luis", SmsNotifierFactory())
    marta = UserSubscriber("Marta", PushNotifierFactory())

    # Suscribir observadores al tema
    topic.attach(ana)
    topic.attach(luis)
    topic.attach(marta)

    # Publicar notificaciones
    topic.publish("Bienvenidos al sistema 👋")
    topic.publish("Se lanzó la versión 3.3 🚀")


if __name__ == "__main__":
    main()
