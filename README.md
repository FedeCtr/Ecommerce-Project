# E-commerce Flask Project

## Descripción

Plataforma de e-commerce desarrollada en Python usando Flask, con dos tipos de usuario: administrador y cliente.  
El proyecto es modular y ordenado, avanzando por etapas y haciendo commits por funcionalidad para mantener un historial limpio.

---

## Estructura de Carpetas

```
ecommerce/
│
├── run.py
├── config.py
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── product.py
│
├── auth/
│   └── routes.py
├── admin/
│   └── routes.py
├── shop/
│   └── routes.py
├── api/
│   └── routes.py
│
├── templates/
│   ├── base.html
│   ├── auth/
│   │   ├── login.html
│   │   └── register.html
│   ├── admin/
│   │   ├── product_list.html
│   │   └── product_form.html
│   └── shop/
│
└── static/
    ├── css/
    ├── js/
    └── img/
```

---

## Etapas de desarrollo y cambios realizados

### Etapa 1: Estructura base y blueprints

- Se creó la estructura inicial de carpetas y archivos.
- Se implementaron los blueprints principales: `/auth`, `/admin`, `/shop`, `/api`.
- Se configuró la app en `run.py` y `config.py`.


---

### Etapa 2: Modelo User y sistema de roles

- Se añadió el modelo `User` en `/models/user.py` con roles (`admin`, `cliente`) y métodos para hash de contraseñas.
- Se integró Flask-Login en el inicio de la app (`run.py`) y se agregó la función `user_loader`.
- El sistema soporta dos tipos de usuarios: `admin` y `cliente`.


---

### Etapa 3: Sistema de autenticación

- Se implementaron rutas para login, registro y logout en `auth/routes.py`.
- Se añadieron plantillas para login y registro en `templates/auth/`.
- Se utiliza hash de contraseñas y roles.
- Se agregaron mensajes flash para feedback.
- Bootstrap para diseño minimalista y responsive.


---

### Etapa 4: CRUD de productos para administrador

- Se añadió el modelo `Product` en `/models/product.py` y se importó en `models/__init__.py`.
- Se implementaron rutas y vistas para listar, crear, editar y eliminar productos en `admin/routes.py`.
- Templates para el listado y formulario de productos en `templates/admin/`.
- Acceso restringido solo a usuarios con rol `admin`.
- Interfaz minimalista y responsive con Bootstrap.


---

## Instalación y ejecución

1. Instala dependencias:
   ```
   pip install Flask Flask-SQLAlchemy Flask-Login PyMySQL Werkzeug
   ```
2. Configura tu base de datos en `config.py`.
3. Ejecuta la app con:
   ```
   python run.py
   ```
4. Accede a las rutas correspondientes para probar cada funcionalidad.

---

## Siguientes etapas

- Listado y compra de productos (cliente)
- Carrito de compras
- Dashboard del admin con estadísticas
- API RESTful
- Integración de método de pago (Stripe/MercadoPago)
- Estética visual final y responsive

---
### Etapa 5: Listado y compra de productos para el cliente

- Rutas y vistas para que los clientes puedan ver el listado de productos y el detalle de cada uno.
- Opción para agregar productos al carrito (carrito básico en sesión).
- Interfaz rápida y minimalista usando Bootstrap.
- Solo usuarios autenticados pueden agregar productos al carrito.

---