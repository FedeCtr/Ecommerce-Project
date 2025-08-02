# E-commerce Flask Project

## Cambios en la etapa 2

- Se añadió el modelo `User` en `/models/user.py` con roles y métodos de autenticación.
- Se integró Flask-Login en el inicio de la app (`run.py`) y se agregó la función `user_loader`.
- El sistema soporta dos tipos de usuarios: `admin` y `cliente`.
- Listo para avanzar con autenticación y gestión de usuarios.

## Siguiente paso

Para crear la tabla de usuarios en MySQL:

1. Ejecuta la app una vez para que SQLAlchemy cree las tablas:
   ```
   python run.py
   ```
2. Verifica la tabla `users` en tu base de datos.

---