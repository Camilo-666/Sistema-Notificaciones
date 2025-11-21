Sistema de Notificaciones

Proyecto académico desarrollado para la asignatura **Ingeniería de Software 2**.

---

Descripción general
Este sistema implementa los patrones de diseño **Observer** y **Factory Method** en lenguaje **Python**, con el propósito de gestionar un sistema de notificaciones modular, extensible y reutilizable.

---

Patrones de diseño aplicados

🔹 Observer
Permite que múltiples objetos (suscriptores) reciban actualizaciones automáticas desde un sujeto común cuando cambia su estado.

- Sujeto (Subject): `NotificationTopic`
- Observador (Observer): `UserSubscriber`

🔹 Factory Method
Facilita la creación de objetos de tipo `Notifier` sin acoplar el código a clases concretas, fomentando la extensibilidad.

- Fábricas: `EmailNotifierFactory`, `SmsNotifierFactory`, `PushNotifierFactory`
- Productos: `EmailNotifier`, `SmsNotifier`, `PushNotifier`

---

Estructura del proyecto

Notificaciones/
├── main.py
├── subject.py
├── observer.py
├── notifier_factory.py
├── notifiers.py
├── user_subscriber.py
└── Diagrama UML.png

---

Funcionamiento
1. Se crean los suscriptores (`UserSubscriber`) con sus respectivos canales de notificación.
2. Cada suscriptor se registra en el tema principal (`NotificationTopic`).
3. Cuando el tema publica un mensaje, los suscriptores reciben la notificación según su canal (Email, SMS o Push).

Ejecutar el sistema:
```bash
python main.py

---

👤 Autor
Camilo Martinez  
Estudiante de Ingeniería de Sistemas  
Universidad Uniremington


