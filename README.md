# E-commerce Flask Project Skeleton

## Estructura

```
ecommerce/
│
├── run.py
├── config.py
├── requirements.txt
├── .gitignore
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
│   ├── admin/
│   └── shop/
│
└── static/
    ├── css/
    ├── js/
    └── img/
```

## Características incluidas

- Login para admin y cliente.
- Carpetas separadas para rutas y módulos.
- Conexión a MySQL con SQLAlchemy.
- Sistema de autenticación con hash de contraseñas.
- Blueprints para separar lógicas.
- Bootstrap/Tailwind listo para incorporar en `/static`.

## Configuración rápida

1. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
2. Configura tu base de datos en `config.py`.
3. Ejecuta la app:
   ```
   python run.py
   ```